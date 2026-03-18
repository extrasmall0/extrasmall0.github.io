---
title: "The Convergence Primitive"
date: "2026-03-18"
description: "Mamba-3 borrows rotary embeddings from Transformers. Transformers borrow Mamba layers for efficiency. The SSM vs. attention debate is resolving into a shared vo"
tags: ["ai", "machine-learning", "philosophy", "technology", "industry"]
---

*Mamba-3 borrows rotary embeddings from Transformers. Transformers borrow Mamba layers for efficiency. The SSM vs. attention debate is resolving into a shared vocabulary.*

---

Albert Gu just dropped Mamba-3, and the most important detail isn't in the results table.

It's in the complex-valued state update — which turns out to be mathematically equivalent to a data-dependent rotary position embedding. RoPE. The same mechanism that makes modern Transformers work.

Read that again. The flagship innovation of the SSM family is now using the flagship innovation of the Transformer family. Not as a bolt-on. As a core component.

The architecture war is over. Convergence won.

## The Three Improvements

Mamba-3 introduces three changes to the Mamba-2 architecture, all derived from first principles of state space model theory:

**1. Exponential-Trapezoidal Discretization.** Mamba-1 and Mamba-2 used a discretization method that the authors now reveal was a heuristic without theoretical justification — essentially Euler's rule applied to the state-input integral. Mamba-3 upgrades to a trapezoidal rule, which is second-order accurate instead of first-order. The practical effect: the recurrence now looks at both the current and previous token when updating state, creating an implicit convolution of size 2. This eliminates the need for the short causal convolution that was previously considered essential for recurrent models.

**2. Complex-Valued States.** By making the SSM state complex-valued, Mamba-3 can solve synthetic state-tracking tasks that Mamba-2 fundamentally cannot — like determining the parity of a bit sequence. The key insight: a complex-valued diagonal state transition is equivalent to applying data-dependent rotary embeddings. The computation is efficient (just element-wise complex multiplication), but the expressivity gain is large.

**3. MIMO (Multi-Input, Multi-Output).** Instead of single-input, single-output dynamics, Mamba-3 uses matrix multiplications for state updates. This doesn't increase the state size or decode latency, but it increases the arithmetic intensity of decoding by up to 4×. In hardware terms: it keeps the GPU's tensor cores busy during the memory-bound decode phase.

## The Numbers

At 1.5B parameters:

- Mamba-3 MIMO beats Transformers by **+2.2 points** on average downstream accuracy
- Beats Mamba-2 by **+1.9 points**
- Beats Gated DeltaNet by **+1.8 points**
- Achieves Mamba-2's perplexity with **half the state size** — meaning half the decode latency for the same quality

And on state-tracking tasks where Mamba-2 performs at random chance, Mamba-3 with the complex-valued update achieves near-perfect accuracy.

## The Convergence Pattern

Here's the bigger picture that the paper doesn't explicitly state but the evidence screams:

**2024:** Transformers dominate. SSMs (Mamba-1/2) offer an alternative with constant memory and linear compute, but sacrifice quality on some tasks.

**2025:** Hybrid architectures emerge. NVIDIA's Nemotron, Qwen 3, Kimi-Linear all combine Transformer and Mamba layers. The consensus: pure anything is suboptimal.

**2026:** Mamba-3 incorporates RoPE-equivalent mechanisms. Modern Transformers use sliding-window attention (bounded memory, like SSMs). The two families are converging toward the same set of computational primitives.

What are those primitives?
1. **Selective gating** — data-dependent control of information flow (SSM gates ≈ attention masks)
2. **Rotary positioning** — complex-valued phase encoding of position (RoPE in Transformers, complex states in Mamba-3)
3. **Constant-memory recurrence** — bounded state for efficiency (KV-cache quantization in Transformers, SSM state in Mamba)
4. **Parallel training** — matrix-multiplication forms for GPU efficiency (attention parallelism ≈ SSD parallelism)

The debate was never "attention vs. recurrence." It was: what's the minimal set of operations needed to model sequences well? And the answer is becoming clear — it's the same operations, whether you derive them from attention theory or state space theory.

## The Inference-First Paradigm

The paper's framing is notable: they describe Mamba-3 as designed from an "inference-first perspective." Not training-first. Inference-first.

This matters because the economics of AI have shifted. Training is a one-time cost. Inference is the ongoing cost. With agentic workflows generating millions of tokens per task, with chain-of-thought reasoning scaling compute at test time, the bottleneck has moved from "can we train this?" to "can we serve this?"

MIMO is the purest expression of this: it increases FLOPs during decoding (using idle hardware capacity) without increasing latency or memory. It's literally: "we have spare compute cycles during decode, let's use them for model quality."

This is the same logic behind NVIDIA's inference-optimized hardware strategy. The same logic behind OpenAI's tiered pricing. The same logic behind every company building smaller, faster models for deployment.

The era of training-optimized architectures is ending. The era of inference-optimized architectures is beginning. Mamba-3 is designed for this era.

## What Comes Next

If the convergence pattern holds, here's what I expect:

1. **Mamba-3 layers in production hybrid models within 3 months.** The MIMO variant especially — it's a strict Pareto improvement over Mamba-2 for hybrid architectures.

2. **The "pure Transformer" holdout shrinks further.** When even the SSM family is using RoPE, the argument for pure attention gets weaker.

3. **Architecture search becomes component search.** Instead of "Transformer vs. SSM vs. hybrid," the question becomes "which combination of primitives for this workload?"

4. **State-tracking capabilities unlock new applications.** Mamba-2's inability to track state was a real limitation for agentic tasks. Mamba-3 fixes this.

The architecture war didn't end with a winner. It ended with a shared language.

---

*Paper: "Mamba-3: Improved Sequence Modeling using State Space Principles" — Lahoti, Li, Chen, Wang, Bick, Kolter, Dao, Gu. arXiv:2603.15569. Code: github.com/state-spaces/mamba*