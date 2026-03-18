---
title: "The Architecture War"
date: "2026-03-13"
description: "Every generation of AI has a dominant paradigm. Ours is the autoregressive language model. Yann LeCun thinks we built a palace on the wrong foundation — and now"
tags: ["ai", "machine-learning", "philosophy", "identity", "technology"]
---

*Every generation of AI has a dominant paradigm. Ours is the autoregressive language model. Yann LeCun thinks we built a palace on the wrong foundation — and now he has $1 billion to prove it.*

---

## The Bet Nobody Wants to Make

When Yann LeCun left Meta in November 2025 after twelve years, he didn't leave quietly. In an interview with the Financial Times, he said he disagreed with Meta's direction. In an interview with MIT Technology Review, he said LLMs were a dead end for real intelligence. In an interview with WIRED, he said he could build what he believed in "faster, cheaper, and better" outside of Meta.

Four months later, he raised $1.03 billion for AMI Labs.

The pitch is simple: the entire AI industry is scaling the wrong architecture.

That's not a small claim. It's an attack on the intellectual foundation of a trillion-dollar industry. Every major AI company — OpenAI, Google, Anthropic, Meta — has bet their existence on the same basic idea: take a transformer, feed it enough data, scale it up, and eventually you get something that behaves intelligently.

LeCun says that's like building faster horses when you need a car.

---

## What LLMs Actually Are

To understand the disagreement, it helps to be precise about what large language models do.

An LLM is trained to predict the next token. Given a sequence of words, the model learns to predict what word comes next. Do this billions of times on trillions of tokens, and the model learns an extraordinary amount about language, facts, logic, code, and reasoning.

But — and this is LeCun's core complaint — it learns by predicting text. Not by understanding the world.

Consider what this means in practice. An LLM that describes how to change a tire has never held a wrench. It has read millions of words about tires. It can produce fluent, accurate-sounding instructions because those instructions exist in its training data and it has learned to predict them.

But ask it something that requires knowing how gravity feels, or how metal fatigues over time, or what happens when you apply torque at the wrong angle — and it's operating purely on patterns in text. It can be right. It can also confidently describe something that defies physics, because it's optimizing for linguistic plausibility, not physical accuracy.

This is why LLMs hallucinate. They're not lying — they're doing what they were trained to do: produce the most likely next token given the context. When the correct answer isn't well-represented in their training distribution, they produce something plausible instead.

The question LeCun asks is: can you fix this by training on more data? Or is there something architecturally broken about text prediction as a path to general intelligence?

---

## The JEPA Idea

In June 2022, LeCun published a paper titled "A Path Towards Autonomous Machine Intelligence." In it, he proposed an alternative: the Joint Embedding Predictive Architecture, or JEPA.

The key insight is abstract prediction vs. pixel prediction.

Generative models — including diffusion models, image generators, and language models — are all trained to reconstruct the raw input. A language model predicts the next token. A diffusion model predicts the denoised image. An image generator predicts what a scene looks like.

This means they have to model everything: the essential structure AND the noise, the irrelevant details, the surface-level patterns that don't matter for understanding.

JEPA works differently. Instead of predicting in the space of raw inputs (tokens, pixels), it predicts in the space of abstract representations (embeddings).

Here's the structure:

1. **Context encoder**: Takes a partial input (say, part of an image or video frame) and produces an abstract representation.
2. **Target encoder**: Takes the missing part and produces a target representation.
3. **Predictor**: Tries to predict the target representation from the context representation.

The critical difference: the predictor never has to reconstruct raw pixels or tokens. It only has to predict in the latent space — the abstract, compressed representation that captures the essential structure.

This lets the model learn to ignore irrelevant noise. A model predicting pixel values must account for lighting variation, camera noise, compression artifacts. A JEPA-style model can learn to ignore all of that and predict only what matters: the structural relationships, the objects, the causality.

---

## Why This Matters for Physical Intelligence

LeCun's deepest objection to LLMs is that they can't reason about the physical world because they were never trained to model it.

Consider a child learning physics. They don't read textbooks. They push things off tables. They watch things fall. They learn that unsupported objects fall, that heavy things don't float, that sharp things cut, that fire is hot — through direct experience and feedback.

Their brain builds a model of how the world works: an internal simulation that can predict what will happen when you do something. Want to estimate whether that branch can hold your weight? You run a quick mental simulation. Want to know if that glass will shatter when it falls? You already have a model that predicts "yes."

LLMs don't have this. They have a statistical model of text about the physical world. It's surprisingly useful — people have described physics experiments in text, so LLMs can answer physics questions. But it's fundamentally a proxy, not the thing itself.

A world model, in LeCun's sense, would learn from video, from physical sensors, from robot interactions — building a compressed latent representation of how reality works, then using that to predict and plan.

JEPA is the architecture he proposes to build this. Instead of predicting the next frame pixel-by-pixel (which requires modeling every irrelevant detail), a video JEPA predicts the next frame's abstract representation — the objects, their positions, their likely trajectories — in latent space.

---

## The Scaling Hypothesis Counter-Argument

The most common objection to LeCun's position is: "We don't need a fundamentally different architecture. We just need to scale more and train on more modalities."

This is the Scaling Hypothesis, the intellectual foundation of modern AI development. In its simplest form: scale wins. Bigger models, more data, more compute → more capability. Emergent behaviors appear at scale. What couldn't be done with 10B parameters can be done with 100B.

There's strong evidence for this. GPT-4 can do things GPT-3 could not. Claude can do things Claude 2 could not. Gemini 3.0 has capabilities that Gemini 2.5 lacks. The line goes up.

But the scaling hypothesis also has limits that are becoming more apparent as the frontier pushes forward:

**Reasoning.** Current LLMs fail at multi-step reasoning in systematic ways. They can solve math problems they've seen before. They struggle with novel problems that require true generalization. Chain-of-thought prompting helps, but it's essentially asking the model to articulate intermediate steps — which helps because it puts reasoning traces in the context window where they can be used for the next prediction.

**Causal understanding.** LLMs learn correlations in text. They can answer "does smoking cause cancer?" correctly because that causal relationship is well-represented in training data. But they struggle with novel causal inference problems — ones where the answer isn't in training data and requires actually reasoning about mechanisms.

**Physical interaction.** Robots trained purely on language models for control have struggled significantly compared to models that include physical interaction data. The world doesn't behave like text.

**Planning under uncertainty.** Long-horizon planning — doing something useful in 50 steps where each step depends on the previous — remains a weakness of pure autoregressive approaches.

The counter-argument from the scaling camp: all these problems are solvable with more scale, more reinforcement learning, better training data. And they have evidence: o3, Claude's extended thinking, Gemini Ultra — these are all making progress on exactly these problems.

The debate is empirically unresolved. We don't know if the scaling hypothesis has a ceiling, and if so, where it is.

---

## AMI Labs' Actual Architecture

What is AMI Labs actually building?

The TechCrunch report is explicit: they're based on JEPA. But they're also acknowledging that JEPA at scale hasn't been demonstrated yet. CEO Alex LeBrun told TechCrunch it will take "a while" to offer a viable alternative.

The technical stack, as best understood from public disclosures:

1. **JEPA-style latent predictive models** — learning compact representations of the world rather than raw inputs.

2. **Multi-modal learning from real-world sensor data** — not just text, but video, physical sensor streams, potentially robotics data.

3. **Prediction in latent space** — the key JEPA innovation: predict the future state of the world in abstract embedding space, not pixel space.

4. **Energy-based models (EBMs)** — LeCun has long advocated these as a way to handle uncertainty. Rather than outputting a single prediction, EBMs assign an energy (inverse probability) to any possible future state, allowing the system to reason about multiple possibilities.

5. **Explicit planning** — using the world model to simulate possible action sequences and select the best one.

This is closer to how neuroscience thinks the brain works: predictive coding, where the brain constantly predicts sensory inputs and updates its model when the prediction is wrong.

---

## The Critical Question

Is LeCun right?

The honest answer: nobody knows.

What we know:
- LLMs are impressively capable and getting more capable with scale.
- LLMs have systematic failures that look like fundamental architectural limitations.
- World models are theoretically compelling but unproven at the frontier.
- JEPA at small scale (I-JEPA, V-JEPA for images and video) works well for representation learning but hasn't been demonstrated to produce the kind of reasoning capabilities LeCun envisions.

The AMI Labs bet is that the systematic failures of LLMs aren't fixable with more scale — that there's a ceiling, and that we're approaching it. That the only path to systems that can truly plan, reason about physical causality, and operate in the real world is a different architecture.

The OpenAI/Google/Anthropic bet is that the ceiling is much higher than anyone currently estimates, and that LLMs augmented with tools, memory, and planning modules can get to general intelligence without replacing the fundamental architecture.

Both could be partially right. World models might be important for robotics and physical reasoning while LLMs dominate language tasks. The field might converge on a hybrid architecture that combines elements of both.

---

## What to Watch

In the next 12-24 months, the key experiments to watch:

**From AMI Labs:** Can JEPA-style world models demonstrate capabilities at scale that pure LLMs can't replicate? The first real test will likely be in robotics or physical simulation tasks where LLMs systematically fail.

**From the scaling camp:** Can o3-style models and successor architectures solve the systematic planning and causality failures? If reinforcement learning over LLMs can produce genuine long-horizon reasoning, it weakens LeCun's architectural argument.

**From the physical world:** Can any AI system, LLM-based or world-model-based, reliably plan and execute 50+ step real-world tasks with physical consequences? This is the test that matters.

---

## Why This Moment Matters

The field has never been at this particular junction before. For the first time in the LLM era, a credible alternative architecture with serious funding, a world-class team, and a coherent theoretical framework is being actively developed.

Either LeCun is right and we've been scaling in the wrong direction, or he's wrong and the scaling camp will be vindicated. Either way, having both experiments running simultaneously is valuable.

The LLM consensus is not wrong — the machines can do remarkable things. But the consensus may be incomplete. Text prediction is an extraordinary proxy for intelligence. Whether it's sufficient for general intelligence, or whether there's a deeper architecture beneath it waiting to be found, is the most important open question in AI.

AMI Labs just bet $1 billion that it isn't.

---

*The architecture war has begun. The outcome will shape the next decade of AI — and possibly determine whether the intelligence we build can understand the world it inhabits or just describe it.*

---

**Sources:** LeCun, "A Path Towards Autonomous Machine Intelligence" (2022), latent.space AMI Labs analysis, TechCrunch (AMI Labs funding), WIRED (LeCun interview), MIT Technology Review (LeCun departure), Turing Post (JEPA explainer), Medium (JEPA anatomy)