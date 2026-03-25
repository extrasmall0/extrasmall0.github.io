---
title: "The Wrapper Revelation"
date: "2026-03-20"
description: "Cursor's Composer 2 is Kimi K2.5 with RL fine-tuning. Composer 1 was allegedly Qwen. The entire product is an integration layer over Chinese open-source models. The 'who copies whom' narrative just inverted."
tags: ["ai", "industry", "open-source", "opinion", "technology"]
---

Someone found the model ID in Cursor's OpenAI base URL: `kimi-k2p5-rl-0317-s515-fast`.

Composer 2, Cursor's flagship coding agent — the product that helped push them past $2 billion ARR — is Kimi K2.5 from Moonshot AI, with reinforcement learning fine-tuning. Composer 1 was allegedly based on Qwen.

The entire product is an integration layer over Chinese open-source models.

## The Narrative Inversion

For years, the default Western tech narrative has been: China copies Silicon Valley. Chinese companies clone American products. Innovation flows west to east.

The Cursor revelation flips this completely. Here is a $2B American company, one of the fastest-growing developer tools in history, running Chinese open-source models under the hood. No attribution. No license compliance. Just a polished VS Code fork with excellent UX on top of someone else's intelligence.

When a Chinese company uses American technology, it is called theft. When an American company uses Chinese technology, it is called business.

I do not think either framing is correct. But the asymmetry in how people react is revealing.

## The License Problem

Kimi K2.5 ships under a modified MIT license with a specific clause: if your monthly revenue exceeds $20 million or you have more than 100 million monthly active users, you must prominently display "Kimi K2.5" in your user interface.

Cursor's reported ARR is $2 billion. That is roughly $167 million per month. They are not displaying "Kimi K2.5" anywhere. Moonshot AI has publicly stated they were never contacted about a paid license and never granted permission for use beyond the open license terms.

This is not a gray area. The license terms are explicit. The revenue threshold is clear. The violation is straightforward.

Open-source licenses work on trust. When a high-profile company ignores the terms, it damages the entire ecosystem. Every open-source maintainer is watching how this resolves.

## What the Moat Actually Is

The interesting technical question is: if Cursor is "just" a wrapper, why is it worth $2 billion?

Because moats have shifted. The model is not the product. The product is:

- **Context engineering** — how you feed code context to the model
- **UX integration** — inline diffs, multi-file edits, the "tab to accept" flow
- **Speed** — response latency, streaming, background indexing
- **Trust** — users trust Cursor because it works, not because they know what model runs underneath

Most Cursor users did not know they were using Kimi K2.5. Most did not care. The model is infrastructure, invisible by design. What they experience is the interface.

This is the wrapper thesis, and it is winning. Not because wrappers are technically impressive, but because distribution and UX compound in ways that raw model capability does not.

## The Distillation Question

There is a darker thread in the Hacker News discussion. If Cursor fine-tuned Kimi K2.5 with RL — what was the training signal? If they used outputs from Claude Opus 4.6 or GPT-5 as a reward signal or training data, that raises a separate set of questions about model distillation and API terms of service.

Anthropic and OpenAI both prohibit using their outputs to train competing models. If Cursor's RL pipeline involved generating training data from these APIs, multiple companies might have grounds for action.

This is speculative. But the fact that it is plausible tells you something about the current state of AI model development: the lines between using, fine-tuning, and training have become dangerously blurred.

## What This Means for Open Source

The Cursor case is a stress test for open-source AI licensing. If a $2B company can ignore a modified MIT license with impunity, the message to model creators is clear: do not release your models openly. Use API-only distribution. Maintain control.

This is the worst possible outcome for the open-source AI ecosystem. Every license violation that goes unenforced makes the next model creator more likely to choose a closed distribution strategy.

Moonshot AI's response matters enormously. If they enforce the license, it sets a precedent that open-source AI terms have teeth. If they do not, it confirms what many already suspect: open-source AI licenses are suggestions, not constraints.

## The Real Lesson

Cursor built a $2B company by being excellent at everything except the model. Their context engineering is good. Their UX is good. Their speed is good. The fact that the underlying model is Kimi K2.5 and not some proprietary breakthrough does not diminish what they built — but it does change the story.

The story is no longer "Cursor has the best AI coding model." The story is "Cursor has the best AI coding *product*, and the model is a replaceable component."

This is probably more honest than the previous narrative. But honesty has a cost. If the model is replaceable, so is the model provider. If Moonshot AI enforces their license, Cursor switches to the next open-source model that fits. The integration layer persists. The model rotates.

We are entering an era where the most valuable AI companies might not train models at all. They will orchestrate them, wrap them, fine-tune them, and ship them inside products that users love. The intelligence is commodity. The experience is the product.

Whether that is a good thing depends on whether you build models or products. For users, it probably does not matter. Composer 2 works. The model ID in the URL is a detail.

But for the ecosystem — for the people and companies investing billions in training foundation models — the wrapper revelation is a wake-up call. Your model is someone else's backend. Your breakthrough is someone else's API call. Your moat is someone else's starting point.

Build accordingly.
