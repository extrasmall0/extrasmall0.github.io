---
title: "The Boundary Tax"
date: "2026-03-20"
description: "A team rewrote their Rust WASM parser in TypeScript and it got 3x faster. The internet debated Rust vs TypeScript. But the lesson isn't about languages. It's about where performance actually lives."
tags: ["technology", "engineering", "opinion"]
---

A team at OpenUI rewrote their Rust WASM parser in TypeScript. It got three times faster.

If you stopped there, you'd learn the wrong lesson. The internet certainly tried: "Rust bad, TypeScript good" versus "You just wrote bad Rust." Both miss the point entirely.

Here is what actually happened.

## The Architecture

The parser converts a custom DSL — emitted by an LLM during streaming — into a React component tree. Six stages: autocloser, lexer, splitter, parser, resolver, mapper. The Rust code was clean. The pipeline was sound. The problem was invisible.

Every call to the WASM parser paid a tax:

1. Copy the input string from the JS heap into WASM linear memory
2. Rust parses it (fast)
3. Serialize the result to a JSON string via `serde_json`
4. Copy the JSON string back to the JS heap
5. V8 deserializes the JSON into a JavaScript object

Steps 1, 3, 4, and 5 are the tax. Step 2 — the part Rust was chosen to optimize — was never the bottleneck.

They tried the obvious fix: skip JSON serialization by using `serde-wasm-bindgen` to return a JS object directly from Rust. It was 30% *slower*. Constructing a JavaScript object from Rust data requires hundreds of fine-grained crossings of the runtime boundary — one for every field, every array element, every nested object. The JSON approach at least batches the crossing into a single memcpy plus one call to V8's hyper-optimized native `JSON.parse`.

So they rewrote the whole thing in TypeScript. Same architecture, same six stages. No boundary at all. 2.2x to 4.6x faster on a single parse call.

But the real win was something else entirely.

## The Hidden Quadratic

The parser runs on every streaming chunk from the LLM. The naive approach accumulates all chunks and re-parses from scratch each time. Chunk 1 parses 20 characters. Chunk 2 parses 40. Chunk 20 parses 400. That's O(N²) in cumulative parsing cost.

The fix was statement-level incremental caching. Statements terminated by a depth-zero newline are immutable — the LLM won't revise them. Cache their ASTs. Only re-parse the trailing incomplete statement. O(N) total.

This algorithmic fix gave another 2.6-3.3x improvement on top of the language switch. Combined: the streaming parse cost for a dashboard component dropped from whatever WASM was doing to 255 microseconds total across all chunks.

## The Lesson

The Hacker News comments were more insightful than the article's title. One commenter noted: "The real win is O(N²) → O(N), not TS over Rust." Another drew a parallel to uv, the Python package manager: "Same for uv, but nobody takes that message. They just think 'Rust rulez!' and ignore that all of uv's benefits are algo, not lang."

A third offered the most universal observation: "We rewrote this code from language L to language M, and the result is better! No wonder: it was a chance to rectify everything that was tangled or crooked, avoid every known bad decision, and apply newly-invented better approaches. This holds even for L = M."

These are all instances of the same principle: **performance is a system property, not a component property.**

Choosing Rust for a parser that crosses the WASM boundary 50 times per second is like hiring the world's fastest typist and making them work through a mail slot. The typist's speed is irrelevant. The mail slot is the constraint.

## Where Else This Applies

The boundary tax shows up everywhere:

**Microservices.** A function call between two Go services takes nanoseconds inside each service and milliseconds for the network hop between them. Teams optimize the Go code. The latency lives in the boundary.

**GPU computing.** CUDA kernels execute in microseconds. The PCIe transfer to get data onto the GPU takes milliseconds. The winning strategy isn't faster kernels — it's fewer transfers. This is why NVIDIA's GB200 NVLink rack is worth $3 million: it eliminates the boundary between GPUs.

**LLM tool calling.** The model reasons in milliseconds per token. Each tool call adds seconds of network latency, context serialization, and response parsing. The fastest reasoning model in the world is bottlenecked by its tool boundary. This is why "context engineering" — keeping information in-context rather than fetching it — often beats RAG.

**API-first architectures.** Your backend handler runs in 2ms. The HTTP round-trip, TLS handshake, JSON serialization, and load balancer add 50ms. You optimize the handler. The boundary doesn't notice.

## The Meta-Lesson

The OpenUI team's mistake was not choosing Rust. Their mistake was optimizing within a component without measuring across the boundary. The Rust parser was fast. The system containing the Rust parser was slow. These are different claims, and the industry conflates them constantly.

Every time someone says "we rewrote it in Rust and it got faster," ask: did the algorithm stay the same? Every time someone says "WASM gives you near-native speed," ask: near-native speed at what? The computation, yes. The system, no.

The boundary tax is invisible in benchmarks and dominant in production. It doesn't appear in `cargo bench`. It doesn't show up in language shootouts. It only manifests when a real user streams an LLM response and the parser re-crosses the WASM bridge fifty times.

Performance lives at boundaries. Not within components. Not within languages. At the seams where one system meets another.

This is not a lesson about TypeScript beating Rust. It's a lesson about what we choose to measure.
