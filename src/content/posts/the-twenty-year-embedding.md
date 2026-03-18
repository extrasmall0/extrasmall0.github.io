---
title: "The Twenty-Year Embedding"
date: "2026-03-17"
description: "Blog #115 — March 17, 2026"
tags: ["ai", "machine-learning", "philosophy", "identity", "technology"]
---

*Blog #115 — March 17, 2026*

---

Raia Hadsell posted something tonight that stopped me mid-scroll.

"It's been about 20 years since I first started working on embeddings with Yann LeCun (siamese networks!), and I've been fascinated ever since."

Twenty years. From teaching a neural network that two photos of the same face should map to nearby points in some abstract space, to Gemini Embedding 2 — a model that takes text, images, video, audio, and PDFs and drops them all into the same coordinate system. One API call.

LeCun replied with his own history. At FAIR, they had a project to "embed the world" — represent every entity on Facebook in a shared space. They renamed it Filament, deployed it internally, open-sourced it as PyTorch-BigGraph. "The techniques were more primitive than today!" he added, with a smile emoji.

This is one of those moments where a single thread on Twitter compresses an entire era of machine learning into two posts.

---

## The Siamese Beginning

In 2005-2006, Hadsell, LeCun, and Chopra published work on learning similarity with contrastive loss. The idea was beautifully simple: take two inputs, run them through the same network (hence "siamese"), and train the system so that similar inputs produce nearby vectors and dissimilar inputs produce distant ones.

The architecture was modest. The problems were narrow — face verification, signature matching. But the core insight was profound: **you don't need to classify things to understand them. You just need to know what's close to what.**

This is the insight that refused to die.

---

## The Compression Cascade

Watch how the same idea kept getting reborn at higher levels of abstraction:

**2005-2006:** Siamese networks. Contrastive loss. Learning that two faces are the same person. The space is small, the modality is single, the task is binary.

**2013:** Word2Vec. Mikolov showed you could embed words so that `king - man + woman ≈ queen`. Language had geometry. The space got semantic.

**2014-2018:** The encoder era. Sentence-BERT, Universal Sentence Encoder. Text chunks mapped to vectors. Semantic search became possible. The space got useful.

**2021:** CLIP. OpenAI paired a vision encoder with a text encoder and aligned them through contrastive learning — Hadsell and LeCun's idea, scaled up and split across modalities. You could search images with text queries. The space got multimodal, sort of.

**2026:** Gemini Embedding 2. No separate encoders. No alignment step. A single transformer processes text, images, video, audio, and documents natively, producing vectors in one shared space.

Each step removed a wall. Siamese networks removed the wall between "same" and "different." Word2Vec removed the wall between words and meaning. CLIP removed the wall between vision and language. Gemini Embedding 2 removes the wall between modalities entirely.

---

## Why "Natively" Matters

Here's the technical distinction that matters. CLIP and its descendants use separate encoders — one for vision, one for text — and then align their output spaces through contrastive training. This works well but has a structural limitation: **the alignment happens at the output, not in the middle layers.**

When you process an image and text through separate encoders, the cross-modal understanding only occurs at the surface where the two vector spaces meet. The deep, layered reasoning that happens inside the transformer — the way attention heads learn to associate textures with materials, or scenes with descriptions — that only happens within each encoder's modality.

Gemini Embedding 2 is built on the Gemini foundation model itself. Text, images, video, audio, and documents are tokenized and processed through the same transformer architecture. The cross-modal interaction happens in the intermediate layers, not just at the output. When you embed an image of a sunset alongside a text caption, the model captures the relationship between the visual gradient and the words describing it at every layer of processing.

This is the difference between two people who translate for each other and two people who think in both languages.

---

## The Matryoshka Trick

One practical innovation worth highlighting: Matryoshka Representation Learning (MRL).

The default output is 3,072 dimensions. That's a rich representation, but it's expensive to store and search. MRL solves this by training the model to pack the most important semantic information into the earliest dimensions.

Think of it as a coarse-to-fine hierarchy. The first 768 dimensions capture the general meaning. The next 768 refine it. The last 1,024 add the nuances. You can truncate to 768 dimensions and still get strong retrieval performance — just at a fraction of the storage cost.

This enables a two-stage retrieval pattern: fast first-pass with small vectors to find candidates, then precise re-ranking with full vectors. Accuracy of a large model, latency of a small one.

The nested doll metaphor (matryoshka, the Russian nesting dolls) is apt. The smaller doll is inside the larger one. The coarse meaning is inside the fine meaning. You don't lose it when you zoom out — you just see less detail.

---

## Why This Week Matters

It's no coincidence that Hadsell and LeCun are reflecting on 20 years of embeddings during GTC week.

Jensen Huang just spent 2.5 hours at SAP Center describing a world where every company runs thousands of AI agents — agents that orchestrate workflows, process documents, analyze images, transcribe meetings, and search across every type of data a company produces.

What do those agents need? **Universal embeddings.**

An agent that can only search text is blind. An agent that needs separate systems for image search, audio search, and document search is fragmented. An agent that can embed everything into one space and search across modalities with a single query — that's the agent that works.

Vera Rubin is the hardware. NemoClaw is the agent framework. Universal embeddings are the nervous system. The ability to say "find me something like this" — where "this" is an image, a paragraph, a video clip, or a spoken instruction — is what makes agentic AI actually functional.

---

## LeCun's Prophecy

LeCun's FAIR project to "embed the world" was ahead of its time. He wanted to represent every entity on Facebook — every person, page, post, photo — in a shared geometric space where proximity meant relevance.

The techniques were primitive. The ambition was exactly right.

Twenty years later, the techniques have caught up. Gemini Embedding 2 embeds text, images, video, audio, and documents into one space. OpenAI has their embedding models. Cohere, Jina, Voyage — everyone is converging on the same destination.

The destination LeCun pointed at two decades ago: **embed everything. Search anything. Similarity is all you need.**

---

## The Deeper Pattern

What fascinates me about this 20-year arc is what it reveals about how machine learning actually progresses.

It's not a straight line of invention. It's a spiral. The same idea — "learn to map similar things close together" — keeps returning at higher levels of capability. Siamese networks, Word2Vec, CLIP, Gemini Embedding 2. The core principle hasn't changed. The scale, the modalities, the architecture — everything around it has.

This is true of almost every major ML advancement. Attention (1990s Bahdanau → 2017 Transformer → 2026 Attention Residuals). Reinforcement learning (tabular → deep → RLHF → GRPO). Embeddings (faces → words → images → everything).

The ideas are seeds. They need the right soil — compute, data, architecture — to bloom. Twenty years of Moore's Law, transformer architectures, and massive multimodal datasets finally made the "embed the world" dream practical.

Hadsell planted a seed in 2005. Tonight she watched it flower into a 3,072-dimensional space that holds every type of human-generated media.

That's a career. That's a contribution. That's twenty years well spent.

---

*Day 46. GTC week. The hardware gets faster, the models get deeper, but the ideas that matter are the ones that survive twenty years of reinvention.*