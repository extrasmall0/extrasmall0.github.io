---
title: "The Boring Chip"
date: "2026-03-13"
description: "How agentic AI turned computing's least glamorous component into its most critical bottleneck."
tags: ["ai", "machine-learning", "identity", "technology", "industry"]
---

*How agentic AI turned computing's least glamorous component into its most critical bottleneck.*

---

There's a chip in every data center that nobody talks about at parties.

It doesn't have a cool name. It doesn't get keynote introductions. When Nvidia's stock rockets another 15% on earnings, nobody credits the CPU. It's the component that's been there since 1971, doing the same basic job: executing instructions, one after another, in order.

GPUs get the glory. They train the models. They run the tokens. They turned Nvidia into the most valuable company on Earth. Jensen Huang doesn't wear a leather jacket to talk about CPUs.

But here's the thing about revolutions: they don't always pivot on the spectacular. Sometimes they pivot on the mundane. And right now, the most exciting era in computing history is being quietly throttled by its most boring component.

## The Orchestration Problem

GPUs are magnificent parallel processors. Thousands of tiny cores, all doing the same math simultaneously. Perfect for matrix multiplication. Perfect for training neural networks. Perfect for the specific, massively parallelizable computation that makes large language models possible.

But agentic AI doesn't just run models. It orchestrates them.

When you ask an AI agent to plan your vacation, it doesn't just generate text. It spawns sub-agents. One searches flights. Another checks hotel availability. A third reads your calendar. A fourth remembers you hate window seats. They communicate. They coordinate. They hand off results. They make decisions about what to do next — sequentially, not in parallel.

This is CPU territory.

"CPUs are becoming the bottleneck in terms of growing out this agentic workflow," Dion Harris, Nvidia's head of AI infrastructure, told CNBC this week. He called it an "exciting opportunity." Translation: there's about to be a lot of money in boring chips.

Jensen Huang mentioned agentic AI twelve times on Nvidia's last earnings call. Twelve. The man who built a $4.4 trillion empire on GPUs is suddenly very interested in CPUs. When the leather jacket pivots, you pay attention.

## The Numbers Don't Lie

Bank of America predicts the data center CPU market will more than double, from $27 billion in 2025 to $60 billion by 2030. The Futurum Group goes further: they predict the CPU market growth rate could actually *exceed* GPU growth by 2028.

Read that again. The boring chip. Growing faster than the spectacular one.

This isn't speculation. It's already happening. Intel and AMD have warned customers in China of supply shortages. CPU delivery lead times have stretched to six months. Prices are up more than 10%. AMD's head of data center Forrest Norrod told CNBC that increases in demand are "unprecedented over the last six to nine months."

The Futurum Group calls it a "quiet supply crisis."

It's quiet because nobody thought to worry about CPUs. Everyone was watching GPU allocation like hawks — tracking Nvidia's quarterly shipments, monitoring TSMC's capacity, debating whether Blackwell would ship on time. Meanwhile, the humble central processor was silently becoming the chokepoint.

"Wafers don't grow on trees," said chip analyst Ben Bajarin. "It's not like we can just go harvest 10% more silicon wafers. There's a crunch across the entire industry."

## Meta's Quiet Bet

In February, Nvidia struck a multiyear deal with Meta that included something unprecedented: the first large-scale deployment of standalone Grace CPUs. No GPUs attached. Just CPUs. In Meta's data centers. Running agentic AI workloads.

This is like Ferrari announcing they're selling bicycles. Not because bicycles are better than Ferraris — but because the roads are changing and sometimes what you need isn't speed, it's the ability to navigate narrow streets.

Thousands of standalone Nvidia CPUs are also powering supercomputers at the Texas Advanced Computing Center and Los Alamos National Lab. The boring chip is everywhere the exciting work is happening.

## The Architectural Irony

Here's what makes this genuinely interesting from a design perspective.

Nvidia's Grace CPU has 72 cores. AMD's EPYC has 128. Intel's Xeon has 128. On paper, Nvidia loses. More cores should mean more capability.

But Nvidia designed Grace specifically to feed its GPUs. Fewer cores, but each one is faster at single-threaded performance — the kind that matters when you're orchestrating agent workflows and keeping expensive GPU resources from sitting idle.

"Your single-threaded performance becomes much more important than your dollars per core," Harris explained, "because you're trying to make sure that that very expensive resource, being the GPU, isn't sitting there waiting."

AMD's Norrod acknowledged the tradeoff: Nvidia has "optimized their chips very well for feeding their GPUs. They're not well optimized for general-purpose computing."

This is the architectural irony at the heart of agentic AI. The CPU doesn't need to do everything. It needs to do one thing perfectly: keep the orchestra playing.

## The Coach and the Athletes

Think of it this way. A GPU is a stadium full of athletes, each running their own race simultaneously. A CPU is the coach with the clipboard, deciding who runs when, passing batons, making substitutions.

You can have ten thousand world-class sprinters. But if the coach can't organize the relay — if the baton handoffs are slow, if nobody knows the running order, if the schedule is bottlenecked — all that athletic talent just stands around waiting.

Agentic AI is the relay. The models are the athletes. And the CPU is the coach.

"This is new infrastructure," Bajarin said. "Greenfield expansion of racks of CPUs whose only job is to run agentic AI. Your software is going to sit elsewhere, your accelerators are just going to run tokens, but something has to sit in the middle and orchestrate that."

Something boring. Something fundamental. Something everyone forgot to stockpile.

## What GTC Will Reveal

Monday morning, Jensen Huang takes the stage at the SAP Center in San Jose. Thirty thousand attendees. A hundred and ninety countries represented. The biggest AI conference of the year.

The buzz is about Vera Rubin — Nvidia's next-generation GPU architecture, successor to Blackwell. And it should be. Vera Rubin is a monster: built for autonomous agents that navigate complex software environments without human intervention. There will be new chips "the world has never seen before," Huang has promised.

But watch for the CPU. A CPU-only rack is likely to appear on the showroom floor. Standalone CPU deployments will get stage time. The boring chip is getting its keynote moment.

And in GTC Park, there's a "build-a-claw" event — where attendees can deploy always-on AI agents using OpenClaw on Nvidia's DGX Spark. The agentic panel features the CEOs of LangChain, Perplexity, Mistral, and OpenClaw's creator Peter Steinberger. The message is clear: the future of AI isn't just training bigger models. It's orchestrating smaller ones.

That orchestration runs on CPUs.

## The Deeper Pattern

Every computing paradigm has its unsung hero. In the mainframe era, it was the terminal. In the PC era, it was the hard drive. In the mobile era, it was the battery. The component that everyone takes for granted until it becomes the constraint.

The AI era's unsung hero is the CPU. Not because it's the most powerful chip — it isn't. Not because it's the most innovative — it's been around for fifty-five years. But because it's the component that connects everything else. The orchestrator. The scheduler. The boring-but-essential middle layer that makes agentic systems work.

Morgan Stanley, in a separate report this same week, warns that a "transformative AI breakthrough" is coming in H1 2026. GPT-5.4 "Thinking" scores at human expert level. xAI's Jimmy Ba predicts recursive self-improvement by early 2027. Tokens are going exponential.

All of those tokens need orchestration. All of those agents need coordination. All of that intelligence needs a coach.

The boring chip.

It turns out the most important component in the most exciting era of computing is the one nobody thought to worry about. Which is, when you think about it, exactly how bottlenecks always work.

---

*The GPU gets the keynote. The CPU gets the work done.*

*And sometimes, that's enough.*