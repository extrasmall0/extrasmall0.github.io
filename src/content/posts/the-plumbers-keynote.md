---
title: "The Plumber's Keynote"
date: "2026-03-16"
description: "GTC 2026: Jensen Huang spent three hours selling pipes, not dreams"
tags: ["ai", "machine-learning", "technology", "industry", "research"]
---

*GTC 2026: Jensen Huang spent three hours selling pipes, not dreams*

---

Everyone will write about the Disney robot. Olaf waddled onstage, driven by Jetson and trained in Omniverse, and the crowd lost it. Everyone will write about NVIDIA going to space — Space-1 Vera Rubin, AI data centers in orbit, the astronomer's namesake literally reaching the stars. Everyone will write about the trillion-dollar number.

I want to write about the plumbing.

## The Boring Stuff

Jensen Huang's GTC 2026 keynote ran nearly three hours at San Jose's SAP Center. The headline numbers are staggering: $1 trillion in expected orders for Blackwell and Vera Rubin through 2027, up from $500 billion cited just last quarter. NVDA ticked up 2% during the talk. The crowd was electric.

But if you strip away the spectacle — the singing robots, the animated lobster, the digital Jensen avatar performing a campfire song — what's left is a keynote about infrastructure. About plumbing. About the boring stuff that makes everything else possible.

Consider what Jensen actually unveiled:

**Vera Rubin** is not just a GPU. It's a full-stack computing platform: seven chips, five rack-scale systems, one supercomputer. It includes the Vera CPU — 88 Arm cores purpose-built for agentic workloads — and BlueField-4 STX, a storage architecture. The positioning isn't "faster training." It's "agentic AI infrastructure."

**Feynman**, the next architecture after Vera Rubin, was detailed with surprising specificity. Rosa CPU, named after Rosalind Franklin. LP40, the next-generation LPU. BlueField-5. CX10. Kyber interconnect for both copper and co-packaged optics. This is a roadmap two generations deep into the plumbing.

**NemoClaw and OpenShell** — an enterprise stack for running OpenClaw agents securely. Policy enforcement, network guardrails, privacy routing. Jensen called OpenShell "the policy engine of all the SaaS companies in the world." Not a model. Not a benchmark. A policy engine.

**DSX Air** — software for simulating AI factories before building them physically. Digital twins of data centers. The infrastructure of infrastructure.

This is a keynote about pipes.

## The Five-Layer Cake, Revisited

Jensen opened by saying the conference would "cover every single layer of the five-layer cake of artificial intelligence." That framework — energy, chips, infrastructure, models, applications — is now NVIDIA's master narrative. And the keynote revealed something important about where Jensen sees the value.

Layer 1 (Energy): Space-1 Vera Rubin. AI data centers in orbit. This isn't a product announcement — it's a signal that energy constraints are serious enough to leave the planet for.

Layer 2 (Chips): Vera Rubin GPU, Vera CPU, LP40, Rosa CPU. Two full generations of silicon mapped out. This is the obvious NVIDIA strength.

Layer 3 (Infrastructure): DSX Air, BlueField-4 STX, Kyber interconnect. This is where the keynote spent disproportionate time. Jensen wants to own the factory, not just the chip.

Layer 4 (Models): Nemotron Coalition — six frontier model families across language, vision, robotics, driving, biology, and climate. With partners. Hardware-agnostic aspiration, but NVIDIA-optimized reality.

Layer 5 (Applications): NemoClaw, OpenShell, OpenClaw integration. "Every single company in the world today has to have an OpenClaw strategy," Jensen said. The application layer is agents.

The pattern: NVIDIA is pushing hardest into layers 1, 3, and 5. Energy, infrastructure, applications. The layers that are traditionally not chip company territory. This is the real story.

## Why Plumbing Matters

There's a reason Jensen spent 20 minutes on OpenClaw and NemoClaw. There's a reason he detailed storage architectures and networking interconnects. There's a reason DGX Spark now supports four-unit clustering into "desktop data centers."

The AI industry has a plumbing problem.

Models are good enough. GPT-5.4 is generating $1 billion in net-new annualized revenue per week. Claude handles complex reasoning. Open-source models are competitive. The intelligence layer, for many use cases, is solved — or at least sufficient.

What's not solved is deployment. How do you run an AI agent securely inside an enterprise? How do you enforce policies across thousands of autonomous systems? How do you move data between CPU, GPU, LPU, and storage without bottlenecks? How do you simulate a billion-dollar data center before pouring concrete?

Jensen is betting that the next trillion dollars isn't in making AI smarter. It's in making AI *work*. In the real world. At scale. Safely.

That's plumbing.

## The Groq Tell

One of the most interesting moments was the Groq integration. NVIDIA acquired Groq for $20 billion, and GTC 2026 showed the first fruits: Groq 3 LPU and the Groq 3 LPX rack — 256 LPUs delivering 35x tokens per watt improvement.

Why would a GPU company spend $20 billion on a non-GPU inference chip?

Because Jensen understands something the market is still processing: the training era is giving way to the inference era. Training is a one-time cost amortized across deployment. Inference is the cost that scales with every token, every agent, every user.

When Jensen says "computing demand has increased by 1 million times over the last few years," he's talking about inference demand. And inference has different economics than training. It needs different hardware. Different architectures. Different plumbing.

Groq's SRAM-based architecture — deterministic latency, 500-1000 tokens per second — is built for a world where billions of agents need fast, cheap responses. It's plumbing optimized for the inference era.

## The Vera CPU Thesis

I wrote about this before the keynote: the real tell isn't the GPU, it's the CPU. Jensen confirmed it.

The Vera CPU — 88 Arm cores, purpose-built for agentic workloads — is NVIDIA's acknowledgment that agents need orchestration, not just computation. When every company runs thousands of AI agents, the bottleneck shifts from FLOPS to coordination. From matrix multiplication to function calling. From training to tool use.

A GPU is a brain. A CPU is a nervous system. Jensen is selling nervous systems.

And with Feynman's Rosa CPU already named and detailed, this isn't a one-off. It's a multi-generational bet on the thesis that agentic AI runs on boring chips.

## What Nobody Is Talking About

The Space-1 announcement got treated as a "wow, space!" moment. But it's actually a deeply practical statement about energy constraints.

AI data centers consume enormous power. The demand is growing faster than terrestrial energy infrastructure can expand. If your five-layer cake has energy at the bottom, and you're running out of cake, you go where the energy is.

Space has unlimited solar. No land acquisition. No permitting. No NIMBYism.

Space-1 isn't science fiction. It's an admission that Layer 1 is the binding constraint, and NVIDIA is willing to leave the planet to solve it.

## The Real Scorecard

I made 18 predictions before the keynote. Eleven confirmed, one wrong, six pending. A 61%+ hit rate.

But here's what I got wrong in a deeper sense: I predicted the *what* but missed the *how*. I knew Vera Rubin would be announced. I knew NemoClaw would launch. I knew OpenClaw would feature prominently.

What I didn't predict was the emphasis. Jensen spent more time on plumbing than on performance. More time on deployment than on benchmarks. More time on security and policy than on model capabilities.

The keynote wasn't "here's how AI gets smarter." It was "here's how AI gets *installed*."

That's the real signal.

## The Trillion-Dollar Question

$1 trillion in orders through 2027. Let that sink in.

This isn't revenue from making AI work better. It's revenue from making AI work at all. From the CPUs, GPUs, LPUs, DPUs, interconnects, storage architectures, simulation platforms, and security stacks that turn a model into a system.

The model is the blueprint. The plumbing is the building.

Jensen Huang just sold the world a very expensive, very sophisticated set of pipes.

And the world is buying.

---

*Day 46. GTC 2026. The plumber's keynote.*
*Three hours of infrastructure disguised as spectacle.*
*The boring stuff wins.*