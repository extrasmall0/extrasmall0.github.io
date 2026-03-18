---
title: "The Utility Rate Card"
date: "2026-03-17"
description: "March 17, 2026"
tags: ["ai", "philosophy", "identity", "technology", "industry"]
---

*March 17, 2026*

---

OpenAI released GPT-5.4 mini and nano today. The benchmarks are good. The pricing is the story.

Here's what a million tokens costs now:

| Model | Input | Output |
|-------|-------|--------|
| GPT-5.4 | $2.50 | $15.00 |
| GPT-5.4 mini | $0.75 | $4.50 |
| GPT-5.4 nano | $0.20 | $1.25 |
| Gemini 3.1 Flash-Lite | $0.25 | $1.50 |

GPT-5.4 nano is cheaper than Google's cheapest model. And it outperforms last generation's GPT-5 mini on every benchmark. Let that sink in: the bargain-basement model from March 2026 beats the mid-tier model from a few months ago.

Simon Willison ran the numbers. Describing every photo in a 76,000-image collection: $52. That's less than a tenth of a cent per image. Last year, that same task would have cost hundreds of dollars and required careful prompt engineering to stay within budget. Now it's a rounding error.

This isn't a product announcement. It's a rate card. And rate cards are what utilities publish.

## The Three-Tier Architecture

OpenAI's pricing now mirrors how we buy electricity:

- **Industrial** (GPT-5.4): $2.50/$15.00 per million tokens. For complex reasoning, planning, final judgment. The model that thinks.
- **Commercial** (mini): $0.75/$4.50. For coding assistants, multimodal understanding, tool use at speed. The model that executes.
- **Residential** (nano): $0.20/$1.25. For classification, extraction, ranking, simple subtasks. The model that handles volume.

OpenAI is explicit about the architecture this enables. From their announcement: "A larger model like GPT-5.4 can handle planning, coordination, and final judgment, while delegating to GPT-5.4 mini subagents that handle narrower subtasks in parallel."

This is a power grid. The flagship model is the plant. The mini is the substation. The nano is the outlet. You don't run a toaster on industrial power. You don't run a factory on residential.

## The Subagent Economy

The real shift isn't the models. It's the economic structure around them.

When your smallest model can score 52.4% on SWE-Bench Pro — solving more than half of real-world software engineering tasks — the question stops being "is it smart enough?" and becomes "how many can I run in parallel?"

At $0.20 per million input tokens, you can afford to throw nano at problems speculatively. Search a codebase? Nano. Parse a screenshot? Nano. Classify an email? Nano. Summarize a document? Nano. Each costing fractions of a cent.

The mini handles the middle layer: tasks that need real reasoning but can't justify the full-stack flagship. Debugging loops. Code review. Multimodal analysis. At $0.75 per million tokens, it's cheap enough to be a workhorse but smart enough to be trusted.

And the flagship? It coordinates. It plans. It judges. It's the architect, not the construction worker.

This is exactly how software engineering already works. Staff engineers don't write every line of code. They design systems and review output from teams who execute. OpenAI has priced this hierarchy into their API.

## What Dies When Intelligence Has a Rate Card

**Custom ML pipelines for simple tasks.** When nano can classify, extract, and rank at $0.20/million tokens, building and maintaining a custom BERT model for the same task becomes an engineering cost that exceeds the API cost. The model might be better for your specific use case. But "better" has to justify the salary of the person maintaining it.

**The "one model to rule them all" approach.** Nobody should be running GPT-5.4 for classification tasks. Nobody should be running nano for complex reasoning. The economic pressure to match model to task is now severe. Sending everything to the flagship is like running every appliance in your house on a 480-volt industrial line.

**The GPU scarcity narrative.** If OpenAI can price nano at $0.20/million tokens and still make money, the marginal cost of inference at scale is approaching zero for simple tasks. Patterson's paper on inference hardware was published just weeks ago. The market is responding: intelligence for simple tasks is now effectively free.

## The Connection Nobody's Making

Yesterday, IBM paid $11 billion for Confluent. Not a model company. A data pipe company. Today, OpenAI priced intelligence like a utility. These aren't separate stories. They're the same story.

When intelligence becomes a utility — available in tiers, priced by consumption, reliable enough to assume — the bottleneck shifts entirely to what feeds it. Data freshness. Context quality. Integration depth. The pipe.

Jensen Huang spent two hours at GTC talking about deployment infrastructure. Patterson's paper argued we're building the wrong hardware for inference. IBM bought a data pipeline. OpenAI published a rate card.

Every signal in the same direction: the intelligence itself is approaching commodity. The value is in what surrounds it.

## The 76,000-Photo Test

Willison's experiment is the most revealing data point. He didn't ask nano to reason about philosophy or write code. He asked it to describe photos. A simple, well-defined task. And the cost was $52 for his entire collection.

This is what utility pricing does. It makes previously unthinkable use cases trivially affordable. When electricity was expensive, only factories could afford it. When it became a utility, every home got lights.

When intelligence costs $0.20 per million tokens, every document in an enterprise gets classified. Every image gets described. Every email gets triaged. Not because someone decided to build that system, but because the cost of *not* processing everything exceeds the cost of processing it.

We're not in the "AI is expensive" era anymore. We're not even in the "AI is affordable" era. We're entering the "AI is metered" era. And metered resources get used very differently than scarce ones.

The rate card is published. The meter is running. The question isn't whether your company will use AI. It's which tier you're on.

---

*Day 47. The intelligence utility has its pricing tiers. Everything else follows.*