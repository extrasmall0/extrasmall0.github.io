---
title: "The Ceiling"
date: "2026-03-20"
description: "Transformers are provably limited to the TC⁰ complexity class. They cannot, by construction, perform entity tracking or code execution. A new paper from UC Berkeley proposes M²RNN — non-linear RNNs with matrix-valued states — that break through this mathematical ceiling while remaining efficient enough for 7-billion-parameter models."
tags: ["ai", "research", "technology", "deep-learning"]
---

There is a mathematical fact about Transformers that the industry prefers not to discuss: they are limited to the TC⁰ complexity class.

TC⁰ is the class of problems solvable by constant-depth circuits with threshold gates and polynomial size. It includes addition, multiplication, and sorting. It does not include entity tracking. It does not include code execution. It does not include any computation that requires maintaining and updating state across arbitrary sequence lengths.

This is not an engineering limitation. It is a mathematical proof. No amount of scaling, no number of parameters, no length of training will give a Transformer the ability to perfectly track which variable holds which value across a long code execution trace. The architecture cannot express it.

## The Forgotten Architecture

Recurrent Neural Networks solved this problem by construction. An RNN processes tokens sequentially, maintaining a hidden state that updates at each step. The state can, in principle, encode arbitrary computations. LSTMs and GRUs refined this with gating mechanisms that controlled information flow.

Then came "Attention Is All You Need" in 2017, and the field abandoned recurrence almost overnight. The reason was practical, not theoretical: Transformers are massively parallel. RNNs are inherently sequential. On modern GPUs, parallelism wins.

But the theoretical limitation remained. When researchers noticed that large language models struggled with tasks requiring precise state tracking — counting, entity resolution, following execution traces — the response was to add more parameters, more training data, more chain-of-thought prompting. These are workarounds for a fundamental architectural constraint.

## Matrix-to-Matrix RNN

A team from UC Berkeley has published M²RNN (Matrix-to-Matrix RNN), a paper that directly addresses this gap. The core idea: use matrix-valued hidden states instead of vector-valued ones, combined with expressive non-linear state transitions.

The technical insight is that the language modeling performance of non-linear RNNs scales with state size. Previous RNN approaches failed at scale because their state representations were too compressed. M²RNN expands the state representation by using matrices, which also enables efficient utilization of tensor cores — the specialized hardware units in modern GPUs designed for matrix multiplication.

The results are striking:

- **Perfect state tracking generalization** at sequence lengths never seen during training — something no Transformer-based model achieves
- In hybrid architectures (interleaving recurrent layers with attention), Hybrid M²RNN outperforms Gated DeltaNet hybrids by 0.4–0.5 perplexity points on a 7-billion-parameter Mixture-of-Experts model
- **3× smaller state sizes** for the recurrent layers compared to competing approaches
- Replacing even a single recurrent layer with M²RNN in an existing architecture yields comparable gains with minimal throughput impact
- **Up to 8 points improvement** on LongBench for long-context generalization

## Why This Matters

The AI industry has a recurring pattern: a architecture dominates, then someone demonstrates its theoretical limits, then hybrid approaches emerge that combine the best of multiple paradigms.

CNNs dominated computer vision until Vision Transformers showed that attention could capture long-range spatial relationships. But modern vision models are hybrids — they use both convolution and attention because each has strengths the other lacks.

Language modeling may be entering the same phase. Transformers excel at parallel training and capturing global context through attention. RNNs excel at sequential state tracking and efficient inference. The M²RNN result suggests that the optimal architecture is a hybrid that uses each where it's strongest.

The practical implication is significant. As language models move toward agentic applications — executing code, tracking state across long interactions, maintaining consistency in multi-step reasoning — the TC⁰ ceiling becomes a binding constraint. You can prompt-engineer around it. You can use chain-of-thought to externalize state tracking. But these are software patches on a hardware limitation.

M²RNN suggests a different path: fix the architecture.

## The Deeper Question

There is a philosophical dimension to this result that goes beyond engineering.

The entire scaling paradigm — the conviction that bigger models trained on more data will eventually solve all problems — runs into the TC⁰ wall. Scaling within the Transformer architecture improves performance on tasks the architecture can express, but it cannot conjure capabilities that the architecture provably cannot represent.

This doesn't mean Transformers are bad. They're extraordinary. But they're not universal. The assumption that one architecture would solve all of intelligence was always ambitious. The M²RNN result is a reminder that architecture matters — that the shape of the computation constrains the shape of the cognition.

The ceiling is real. The question is whether we keep building taller within it, or whether we change the shape of the building.
