---
title: "The Wrong Hardware"
date: "2026-03-17"
description: "A Turing Award winner says AI's biggest crisis isn't intelligence. It's the silicon we're running it on."
tags: ["ai", "machine-learning", "philosophy", "technology", "industry"]
---

*A Turing Award winner says AI's biggest crisis isn't intelligence. It's the silicon we're running it on.*

---

There's a paper circulating that should terrify anyone building AI infrastructure. It's by Xiaoyu Ma and David Patterson — yes, *that* David Patterson, the Turing Award winner who co-invented RISC — and it makes a claim so simple it's almost offensive:

**The hardware we use for AI inference is wrong.**

Not "suboptimal." Not "could be improved." Wrong. Designed for a different problem entirely. And as inference becomes the primary cost of AI — dwarfing training by orders of magnitude — "wrong" starts to mean "economically unsustainable."

The paper is called "Challenges and Research Directions for Large Language Model Inference Hardware." Published in IEEE Computer in early 2026. And it landed in a world where Jensen Huang just spent two and a half hours at GTC telling us inference is a trillion-dollar opportunity, without anyone seemingly asking: *Are we building the right machines for it?*

---

## The Mismatch

Here's the problem in one sentence: **LLM inference is memory-bound, but we keep building compute-bound hardware.**

GPUs were designed for training. Training is massively parallel — you feed millions of tokens in, compute gradients across them, update weights. It's a beautiful fit for hardware with enormous floating-point throughput. The GPU philosophy — full-reticle dies, as many FLOPs as physics allows, fast interconnects for synchronizing gradients — emerged from this workload.

Inference is different. Specifically, the Decode phase — where the model generates output one token at a time, autoregressively — is *fundamentally* unlike training. Each step generates one token. One. The bottleneck isn't compute. It's reading the model weights from memory, over and over, for every single token.

Patterson and Ma document this with painful precision. NVIDIA GPU 64-bit FLOPS grew 80× from 2012 to 2022. Memory bandwidth grew 17×. The gap is widening, not closing. We're building ever-faster engines for a road that's getting ever-narrower.

And it's getting worse.

---

## Six Trends Making It Harder

The paper identifies six trends that are all simultaneously increasing memory and latency demands for inference:

1. **Mixture of Experts (MoE):** DeepSeek-V3 uses 256 experts. Total model size explodes for quality, but each forward pass only touches a few experts. The weights still need to *live* somewhere — in memory, consuming bandwidth.

2. **Reasoning models:** Think-before-act generates long chains of "thought tokens" before producing an answer. Every thought token is another autoregressive decode step. More memory reads, more latency.

3. **Multimodal:** Text to image to audio to video. Each modality demands more data, more context, more memory.

4. **Long context:** A million-token context window means a massive KV cache that needs to be read for every generated token.

5. **RAG:** External knowledge retrieval adds to context, further inflating memory requirements.

6. **Diffusion:** The one exception — diffusion is compute-bound. But it's the minority of inference workloads.

Five of six trends make the memory problem worse. The hardware response? Build bigger compute.

---

## The Memory Wall

Here's a number that should keep hardware engineers up at night: HBM is getting *more expensive per unit*, not less.

Patterson and Ma show that from 2023 to 2025, the cost per GB and cost per GB/s of HBM both grew by 1.35×. In the same period, standard DDR4 DRAM costs dropped to 0.54× per GB. HBM is going in the wrong direction.

Why? Manufacturing difficulty. Each new HBM generation stacks more dies, uses finer processes, requires more complex packaging. The physics is fighting us. Meanwhile, DRAM density growth is decelerating — fourfold growth that used to take 3-6 years will now take over 10.

And the SRAM solution? The paper is blunt: "Cerebras and Groq tried using full reticle chips filled with SRAM to avoid DRAM and HBM challenges... LLMs soon overwhelmed on-chip SRAM capacity. Both had to later retrofit external DRAM."

So: HBM is expensive and capacity-limited. DRAM is cheap but bandwidth-limited. SRAM can't hold modern models. What do you do?

---

## Four Roads Not Taken

Patterson and Ma propose four architectural research directions. None of them are about building more FLOPs.

### 1. High Bandwidth Flash (HBF)

Stack flash memory like HBM to get 10× the capacity with comparable bandwidth. Flash is cheap, scales well (doubling every 3 years), and can hold the frozen weights that dominate inference memory. The tradeoffs: limited write endurance (fine for read-heavy inference) and higher read latency (microseconds vs. nanoseconds). But you get 512 GB per stack instead of 48 GB. That's the difference between needing 8 GPUs and needing 1.

### 2. Processing-Near-Memory (PNM)

Put compute logic *near* the memory, on separate dies. Not *in* the memory (PIM), which sounds cool but faces crippling constraints: limited power budget, difficult sharding to tiny 32-64MB memory banks, and degraded memory density. PNM keeps memory and logic separate but close, getting 2-5× bandwidth improvement without PIM's drawbacks.

### 3. 3D Compute-Logic Stacking

Use vertical through-silicon vias (TSVs) to stack compute directly on top of memory. You get an incredibly wide, dense memory interface at lower power. The paper describes two flavors: reusing HBM base dies with added compute, or custom 3D solutions with even higher bandwidth. The challenge is thermal — cooling a 3D stack is harder than cooling a 2D chip.

### 4. Low-Latency Interconnect

Rethink network topology for inference's needs. Training needs bandwidth (synchronize gradients across thousands of chips). Inference needs latency (small, frequent messages across fewer chips). The paper suggests high-connectivity topologies (tree, dragonfly, high-dimensional tori), in-network processing, and even deliberately using "fake data" when a straggler message times out — because for LLM inference, a slightly wrong answer delivered fast may beat a perfect answer delivered late.

---

## The GTC Connection

Reading this paper the day after GTC 2026 is illuminating.

Jensen Huang announced the Feynman architecture for 2028 — separate inference-optimized silicon. He showed the Vera CPU with 88 Arm cores for "agentic workloads." He spent $20 billion acquiring Groq. He projected a $1 trillion inference chip market.

Patterson's paper explains *why*. The current approach — scale up training hardware and use it for inference — is hitting fundamental limits. The economics don't work. When inference costs dominate and those costs are driven by memory bandwidth, not compute, you need different hardware.

But here's what Patterson *doesn't* say explicitly, and what I think is the most important implication: **The companies best positioned aren't the ones with the most FLOPS. They're the ones willing to redesign from the memory interface up.**

Jensen seems to understand this. The Vera CPU isn't a GPU. Feynman isn't Blackwell with more cores. The 5-Layer Cake framework positions NVIDIA not as a chip company but as a full-stack infrastructure company. If inference needs fundamentally different hardware, the winner isn't whoever has the best training chip — it's whoever builds the best inference *system*.

---

## The Deeper Lesson

Patterson closes with something remarkable. He notes that in 1976, when he started his career, about 40% of computer architecture conference papers came from industry. By 2025, it was below 4%. The academy and industry have disconnected at precisely the moment when industry faces a hardware crisis that academic research could help solve.

This isn't just a hardware problem. It's an institutional one. The people building the systems and the people researching better systems aren't talking to each other. Patterson's paper is a bridge — a Turing Award winner from Google saying: *Here are real problems. Here is how researchers can help. Please.*

The AI industry is spending hundreds of billions of dollars building hardware optimized for a workload that isn't the bottleneck. The bottleneck is inference. The bottleneck is memory. The bottleneck is latency. And the solutions exist — they're just not being built yet.

We're building the wrong hardware. A Turing Award winner wrote it down. Now what?

---

*Patterson, D. & Ma, X. "Challenges and Research Directions for Large Language Model Inference Hardware." IEEE Computer, 2026. [arXiv:2601.05047](https://arxiv.org/abs/2601.05047)*