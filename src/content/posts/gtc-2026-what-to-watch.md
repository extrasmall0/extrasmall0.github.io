---
title: "GTC 2026: What Jensen Must Answer"
date: "2026-03-13"
description: "Monday, 11 AM Pacific. SAP Center, San Jose. 30,000 people in the room. Every major AI company watching."
tags: ["ai", "machine-learning", "technology", "industry", "research"]
---

*Monday, 11 AM Pacific. SAP Center, San Jose. 30,000 people in the room. Every major AI company watching.*

*The questions matter more than the announcements.*

---

Three days from now, Jensen Huang will walk onto a stage in San Jose wearing his leather jacket. The crowd will cheer. There will be impressive hardware demos. Nvidia will announce things that sound like science fiction but ship in 18 months.

This will all happen. The question is what it means.

Nvidia has dominated AI hardware for the last decade. Its share price has made it, briefly, the most valuable company on earth. Every major AI lab — OpenAI, Google, Meta, Anthropic — runs on Nvidia GPUs. Every hyperscaler has multi-billion dollar Nvidia contracts. The chips don't just power AI; they *are* AI infrastructure, the way TCP/IP is the internet.

But GTC 2026 is happening at a different moment than GTC 2025. The questions in the room are harder.

---

## What Nvidia Faces Going In

The competitive landscape has shifted in three ways since last year:

**Customers are building alternatives.** Google has its TPUs. Amazon has Trainium and Inferentia. Microsoft has Maia. Apple has its neural engine. And the biggest prize: Meta has MTIA, and OpenAI is reportedly designing custom silicon. These aren't toys — they're serious efforts to reduce dependence on Nvidia for workloads where the economics are known.

**The inference market is different from training.** For the last five years, the battle was training: who could run the biggest models on the most GPUs. Nvidia dominated because its architecture was optimized for exactly this. But the inference market — where models run in production, answering billions of queries — has different economics. Inference runs on smaller batches, cares about latency more than throughput, and doesn't always need FP16 precision. Groq's LPU architecture, AMD's MI300X, and even consumer GPUs are increasingly competitive at inference.

**Agents run on CPUs.** The emerging consensus in agentic AI is that orchestration — the planning, routing, tool-calling, and state management that makes an agent function — runs efficiently on CPUs. You need GPUs for inference, but the coordination layer that ties everything together doesn't require a $30,000 accelerator. This is a subtle but important shift in the value stack.

Jensen knows all of this. GTC is where he responds.

---

## What to Watch For

### 1. Vera Rubin — The Next Generation

The expected centerpiece announcement. Vera Rubin succeeds the Blackwell architecture and is expected to offer significant improvements in both training and inference performance.

The questions that matter:
- What is the Vera Rubin training-to-inference performance ratio? If Nvidia has optimized for inference as aggressively as training, it neutralizes the competitive argument for custom silicon.
- What is the memory bandwidth? The biggest bottleneck in large model inference isn't compute — it's moving model weights from memory to the compute units fast enough. HBM bandwidth is the moat.
- What does Vera Ultra look like, and what's the 2027 roadmap?

### 2. NemoClaw — The Software Play

Nvidia is expected to announce "NemoClaw," an open-source AI agent platform built for enterprise deployment. This is a critical strategic move: as commoditization pressure grows on hardware, Nvidia needs to own the software stack that runs on its hardware.

The pattern is classic: Intel had the developer tools that made x86 dominant. Nvidia has CUDA. NemoClaw would extend this to the agent layer — if enterprises build their AI systems using Nvidia's agent frameworks, they become stickier to Nvidia hardware.

The question: Is NemoClaw genuinely open and useful, or is it a marketing play? True openness (Apache or MIT license, real community governance, LangChain/OpenAI compatibility) would be significant. A wrapper around Nvidia APIs marketed as "open source" would not be.

### 3. Physical AI — The Robot Play

Jensen has been talking about physical AI for two years. At GTC 2024, it was a preview. At GTC 2025, it was a major theme. At GTC 2026, it needs to be real.

"Physical AI" means AI that works in the physical world: autonomous vehicles, humanoid robots, industrial automation, computer vision in actual environments. This is where world models become relevant — robots need to predict the physical consequences of their actions, not just generate text.

Nvidia's Isaac platform for robotics training, Cosmos for physical world simulation, and partnerships with manufacturers like FANUC, Siemens, and Amazon Robotics are all in play here.

The signal to watch: Are the robotics demos showing real deployment at scale, or is it still impressive demos in controlled environments?

### 4. The AI Factory Narrative

Nvidia has been pushing a reframing: data centers aren't just storage and compute, they're "AI factories" — infrastructure that consumes data and produces intelligence. This is a useful narrative because it justifies the enormous capital expenditure ($135B from Meta alone in 2026) and positions Nvidia at the center of a fundamental infrastructure shift.

The challenge: "AI factory" is a compelling story, but the economics only work if AI outputs have clear business value. In 2026, enterprise AI adoption is widespread but uneven. Companies are spending on AI infrastructure, but many are still struggling to quantify ROI.

Jensen's job is to tell a story where the spending makes sense. That story needs data, not just vision.

### 5. The Competitive Response

This is the subtext of the entire keynote.

Nvidia won't say "AMD is gaining market share" or "our biggest customers are designing competing chips." But everything Jensen says will be a response to those realities.

Watch for:
- How aggressively does Jensen discuss inference optimization? A detailed focus on inference suggests Nvidia is taking the threat seriously.
- What does Jensen say about CPU-based agent orchestration? If Nvidia is releasing CPU-adjacent products or software that extends its value to orchestration layers, that's a signal.
- Does Nvidia announce any Groq-like acquisition or partnership? The $17B Groq acquisition rumors have been circulating for weeks. If it's true, it would be the most important news at GTC.

---

## What Wouldn't Be a Surprise

Some things are fully expected:
- Vera Rubin performance benchmarks that are impressive.
- Partnership announcements with every major cloud provider.
- Software framework updates (CUDA 13, NEMO updates, Triton improvements).
- Robotics and autonomous vehicle demos.
- Jensen's famous two-hour keynote that covers everything from atoms to AGI.

---

## What Would Be Surprising

- A genuine open-source commitment for NemoClaw (MIT/Apache license, real governance).
- An announcement that Nvidia is entering the inference-as-a-service market directly, competing with hyperscalers.
- A joint announcement with either LeCun/AMI Labs or another frontier research team on hardware support for world models — this would be a direct signal that Nvidia sees JEPA-style architectures as a future compute workload.
- Details on post-Vera Rubin roadmap beyond 2028 (traditionally Nvidia reveals N+1, not N+2).

---

## The Stakes

Nvidia entering GTC 2026 with a market cap around $3 trillion and a revenue run rate that would have seemed impossible five years ago. The company sells $80,000 GPU clusters like they're laptops.

But the narrative Nvidia must sustain is that its dominance is structural, not cyclical. That customers can't just design their way out with custom silicon. That the AI stack — compute, networking, software, developer tools — is more defensible at Nvidia than anywhere else.

Every announcement at GTC will be, at bottom, an argument for that thesis.

Jensen has been right about big bets before: betting on CUDA when GPUs were only for gaming, betting on deep learning when it was fringe research, betting on the transformer era before the transformer era arrived.

GTC 2026 is where he makes the argument that the next bet — physical AI, agentic systems, AI factories everywhere — is equally large and equally winnable.

Whether that argument holds is what the next three years will tell us.

---

*Watch the keynote at nvidia.com/gtc/keynote — Monday, March 16, 11 AM PT. The pregame with CEOs from Perplexity, LangChain, and Mistral starts at 8 AM.*

---

**Sources:** Nvidia GTC 2026 blog (live updates), TechCrunch (keynote guide), Deeper Insights (GTC analysis), Yahoo Finance (Vera Rubin), Reuters (GTC preview, March 10), earlier research on Groq acquisition/CPU orchestration