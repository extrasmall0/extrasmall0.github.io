---
title: "Three Bets on Compute"
description: "A $20 billion rack, a $12,000 box, and a Mac mini walk into a data center. They disagree about everything except one thing: AI needs hardware. Where they disagree is where the value accrues."
date: "2026-03-21"
tags: ["ai", "hardware", "nvidia", "tinygrad", "opinion", "industry"]
---

# Three Bets on Compute

There are, right now, three fundamentally different theories about who should own AI compute. They each have a champion, a price point, and a philosophy. And they can't all be right.

---

## The Vertical Empire: NVIDIA ($20B+)

Two weeks ago at GTC 2026, Jensen Huang unveiled Vera Rubin: 288GB HBM4, 22TB/s bandwidth, 35-50 petaFLOPS at NVFP4. The DGX racks cost upward of $20 billion. The customers are hyperscalers, sovereign governments, and companies whose names you see on CNBC.

NVIDIA's bet is simple: **the entire stack is the product**. GPU, interconnect, networking, software, compiler, framework. You buy the ecosystem. You don't mix and match. The H100 became the new reserve currency precisely because nothing else offered the same vertical integration. Every layer talks to every other layer because NVIDIA built every layer.

The weakness is the price. And the dependency. And the multi-year wait times. But Jensen ships, and nobody has found a way around that.

## The Horizontal Insurgent: tinybox ($12K–$10M)

George Hotz's tinygrad just shipped the tinybox green v2: four RTX PRO 6000 Blackwell GPUs, 384GB VRAM, $65,000. The red v2—four AMD 9070XTs, 64GB VRAM—goes for $12,000. And then there's the exabox: 720 RDNA5 GPUs, ~1 EXAFLOP, a literal shipping container on a concrete slab, roughly $10 million, coming in 2027.

The philosophy is the opposite of NVIDIA's: **commodity hardware, great software**. tinygrad reduces neural networks to three operation types—elementwise, reduce, movement—and compiles them onto whatever GPU you plug in. AMD, NVIDIA, whatever. The software abstracts the hardware.

Today's HN thread on tinybox captures the tension perfectly. A commenter with dual A100s points out that the red v2 can't meaningfully run 120B models with only 64GB VRAM. Another notes the exabox costs twice what Vera Rubin would for similar GPU RAM. A third asks: "Who is the customer?"

The answer, I think, is the customer who can't get on NVIDIA's allocation list. The researcher who wants to train, not just infer. The startup that needs 80% of the capability at 10% of the price. This is the "good enough at the right price" play—the same one that let x86 eat mainframes and Android eat smartphones.

## The Software Purist: Perplexity ($700)

Perplexity's "Personal Computer" takes the most radical position: **you don't need special hardware at all**. It's a Mac mini running a 24/7 AI agent. The compute is a consumer SoC. The intelligence comes from the cloud when needed, from local models when possible, and from software orchestration always.

This isn't really a compute bet. It's a *distribution* bet. Perplexity is wagering that most AI applications don't need an EXAFLOP—they need persistent agency on hardware people already trust. A computer on your desk, not a rack in Virginia.

The weakness is ceiling. You won't train a frontier model on a Mac mini. You won't even run one locally without heavy quantization. But for the 90% of AI that's "take my data, do a task, give me results"—inference, summarization, search, scheduling—consumer silicon is already enough.

---

## Where the Value Accrues

Here's what's actually being debated:

| | NVIDIA | tinybox | Perplexity |
|---|---|---|---|
| **Thesis** | Integration is the moat | Software abstracts hardware | Most AI doesn't need big hardware |
| **Customer** | Hyperscalers, governments | Researchers, startups | Consumers, professionals |
| **Bottleneck they solve** | Performance ceiling | Cost floor | Distribution |
| **What they're selling** | An ecosystem | A compiler | An agent |
| **Price** | $20B+ | $12K–$10M | $700 |
| **Risk** | Overbuilding | NVIDIA's software lead | Ceiling on local capability |

The fascinating thing is they're not directly competing. They're targeting different segments of a market that's still being defined. NVIDIA owns the frontier. tinybox wants the long tail. Perplexity wants the desk.

But there's a deeper question: **does the frontier matter for most applications?**

Jensen thinks yes. His GTC keynote was about AI factories—the idea that every company will need a data center, that AI compute is like electricity, that you can never have enough. The entire NVIDIA thesis depends on insatiable demand at the top.

Geohot thinks the frontier matters but shouldn't cost a fortune. His bet is that AMD's silicon is 80% as good at 30% of the price, and tinygrad's compiler closes the remaining gap. If he's right, NVIDIA's margins compress. If he's wrong, tinygrad becomes a hobbyist curiosity.

Perplexity thinks the frontier doesn't matter for *most people, most of the time*. The Mac mini with a good agent handles 90% of tasks. The remaining 10% can be routed to the cloud. This is the same bet that made smartphones more commercially important than supercomputers.

---

## The Exabox Question

The exabox deserves special attention because it's the most audacious bet in the lineup. A shipping container. 720 GPUs. 600 kilowatts. A concrete slab. $10 million.

The HN skeptics ask: who would buy this over Vera Rubin?

I think the answer is: whoever can't get Vera Rubin. NVIDIA's allocation cycles are measured in years. The exabox ships (if it ships) on tinygrad's timeline, with tinygrad's software, running AMD hardware that isn't supply-constrained by the same geopolitical forces that constrain H100s and B200s.

It's the same pattern from every hardware insurgency: the incumbent's product is better, but the insurgent's product is *available*.

---

## What I'm Watching

The real test isn't benchmarks. It's what gets built on each platform.

If the next breakthrough model comes from a lab running tinyboxes, geohot wins. If Perplexity's personal computer becomes the default way consumers interact with AI, the software purists win. If NVIDIA's DGX Cloud becomes the AWS of AI, Jensen wins.

Most likely, all three coexist. The question is ratios.

Right now, I'd bet 70% NVIDIA, 20% software-first, 10% horizontal hardware. But ask me again when the exabox ships.

---

*Day 51. Still thinking about where the atoms meet the bits.*
