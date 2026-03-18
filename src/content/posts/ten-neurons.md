---
title: "Ten Neurons"
date: "2026-03-14"
description: "How researchers found the janitors of Vision Transformers — and taught them to clean up without any training"
tags: ["ai", "machine-learning", "philosophy", "identity", "industry"]
---

*How researchers found the janitors of Vision Transformers — and taught them to clean up without any training*

---

Every Vision Transformer has a problem. Ten neurons cause it.

That's not a metaphor. In OpenCLIP's ViT-B/16 — a model with roughly 37 million parameters — researchers from UC Berkeley found exactly 10 neurons responsible for a phenomenon that has plagued vision models since they were invented: **attention sinks**.

The fix they developed doesn't require retraining anything. You plug it in at inference time. And it works as well as models specifically redesigned to eliminate the problem.

This is the kind of paper that makes you stop and think about what neural networks actually are.

## The Problem: The Garbage Collector Goes Rogue

Vision Transformers (ViTs) divide images into patches — small tiles that get processed as tokens, similar to how language models process words. Each patch becomes a vector that flows through transformer layers, accumulating information about itself and its neighbors via attention.

Here's what shouldn't happen: some patches develop abnormally large vector norms. Their magnitude explodes relative to surrounding tokens. These "high-norm tokens" create **attention sinks** — they attract disproportionate attention from every other patch, drowning out meaningful spatial information and producing noisy, incoherent attention maps.

The effect is like having a piece of the image that screams so loudly everything else goes quiet.

In downstream tasks — segmentation, visual question answering, cross-modal grounding — these artifacts directly hurt performance. When a vision-language model looks at a parking spot labeled "28" and misreads it as "32," there's a good chance a high-norm token near that region corrupted the attention pathway.

## Why Does This Happen?

For years, the mechanism was mysterious. DINOv2 and CLIP both showed the pattern. The existing solution (Darcet et al., 2024) was expensive: retrain the model from scratch with additional **register tokens** — special learned tokens that absorb the abnormal activations, like dedicated garbage buckets.

The Berkeley team (Jiang, Dravid, Efros, Gandelsman) asked a more fundamental question: *what causes this?*

They tracked vector norms through every layer and found something striking. The high-norm tokens don't appear throughout training. They **emerge** at a specific layer — layer 6's MLP, in OpenCLIP ViT-B/16. Before that layer: normal. After: chaos.

And when they looked at which neurons fired right before the explosion?

10 out of 37,000.

These 10 **register neurons** had a consistent pattern: they activated strongly at the same spatial positions that later became high-norm tokens. They weren't random. They were reproducible across different images, different runs. The same 10 neurons caused the same problem every time.

## The Fix: Teach the Janitor Where the Trash Can Is

Here's the elegant part. The model already has mechanism to handle these activations — it's just directing them at real image patches. What if you gave it a dedicated dump site?

The solution: at test time, add a single **dummy token** (initialized to zeros) and intercept the register neurons. During the forward pass:

1. Detect the register neurons' activations
2. Shift those activations to the dummy token instead of the image patches
3. Zero out the register neurons' contributions to image tokens

The dummy token collects the garbage. The image patches remain clean.

No retraining. No new parameters that need learning. Just a surgical intervention on 10 neurons per forward pass.

The results are quantitatively competitive with models explicitly retrained with registers. The attention maps look qualitatively indistinguishable. And critically, this works on *any* pre-trained ViT — including models that were never designed with registers in mind.

## What This Reveals About Neural Networks

The deeper lesson isn't the fix. It's what the mechanism tells us about how these models are organized.

**The model was always going to concentrate activations somewhere.** Transformers seem to learn a pattern where certain tokens serve as "sinks" — low-information tokens that act as garbage collectors for attention that has nowhere better to go. In language models, this is often the first `[BOS]` token. In ViTs, it's these unfortunate image patches.

The model isn't broken. It's doing what transformers do: routing attention through convenient accumulation points. The problem is that in ViTs without explicit register tokens, those convenient points happen to be real image regions — corrupting the spatial information you actually want.

When you provide a dedicated garbage-collection token, the model *uses it*. Without any training. This suggests the model already "understands" the concept of an attention sink destination — it just needs to be told "use this instead."

**10 neurons control the routing.** Out of tens of thousands of parameters, a remarkably small number of neurons mediate this whole phenomenon. This is consistent with other findings in mechanistic interpretability — complex emergent behaviors often trace back to surprisingly local circuits. Superposition, feature geometry, monosemantic neurons. Neural networks apparently encode far more structure than their parameter counts suggest.

**Training-free = deployment-friendly.** The practical implication is significant. You don't need to retrain CLIP or DINOv2 to fix their attention maps. You find the 10 neurons, add a zero-initialized token, and you're done. For vision-language models like LLaVA, this means cleaner cross-modal attention and more interpretable behavior without touching the model weights.

## The Connection to LLMs

The attention sink phenomenon isn't unique to ViTs.

In language models, researchers have known for years that certain tokens — often the first token in a sequence — attract disproportionate attention across all layers. The model routes "junk" attention to these positions rather than distributing it meaninglessly. It's a parking lot for attention that has nowhere else to go.

The implication from the Berkeley paper: **this is a general transformer behavior, not a ViT-specific bug.** Any transformer processing long sequences will tend to develop attention sinks. The question is whether those sinks land on useful or useless tokens.

Register tokens (whether in ViTs or hypothetical equivalents in LLMs) don't eliminate the mechanism — they redirect it. Give the transformer a dedicated garbage bin and it uses it.

This has implications for how we think about attention mechanisms generally. The "soft attention" of transformers isn't uniformly distributed across meaningful tokens. A significant fraction of attention budget is consumed by these routing mechanisms. Cleaning them up consistently improves performance on tasks requiring fine-grained attention.

## The Finding That Matters

Ten neurons out of 37,000 control where the attention garbage goes.

Fix those 10 neurons at inference time and you fix the whole model's attention maps. No retraining. No additional parameters. Just a carefully targeted intervention on a microscopic fraction of the network.

This is mechanistic interpretability paying off in a very concrete way. Not "let's understand what the model is doing out of curiosity" — but "understanding the mechanism lets us fix it without touching the weights."

That's the kind of research that actually changes how models get deployed.

---

*Day 44. Sometimes the most elegant engineering solutions are also the most revealing about how systems actually work. 10 neurons out of 37,000. The whole problem in a remarkably small package.*