---
title: "The Twenty-Five Megabyte Voice"
date: "2026-03-19"
description: "KittenTTS ships 8 voices in 25 megabytes. No GPU. No API key. No cloud. Voice just became a local file."
tags: ["ai", "technology", "agents", "opinion"]
---

A text-to-speech model that fits in 25 megabytes. Runs on CPU. No GPU required. No API call. No cloud dependency. No usage meter ticking in the background.

KittenTTS shipped three models this week: 80M parameters, 40M, and 15M. The smallest, quantized to int8, is 25 megabytes. For context, that's smaller than most app icons in iOS these days. It comes with 8 built-in voices, runs at 24kHz, and handles numbers, currencies, and units out of the box.

370 points on Hacker News. 146 comments. The developer community noticed.

## Why This Matters

The history of AI capabilities follows a predictable arc: impossible → expensive cloud API → cheap cloud API → runs locally → runs on your watch. We've seen it with image classification, with language models, with image generation. Each step down the stack unlocks a new class of application.

Voice synthesis has been stuck at "expensive cloud API" for years. ElevenLabs, PlayHT, Azure Cognitive Services — brilliant quality, but every syllable costs money and requires an internet connection. That shapes what gets built. You don't build an offline voice assistant if every sentence costs a fraction of a cent and needs Wi-Fi.

25 megabytes changes the calculation. Not because the quality matches ElevenLabs — it probably doesn't, not yet. But because it changes the deployment economics from "pay per phoneme" to "copy this file."

## The Edge Is the New Cloud

Think about what this enables:

**Embedded devices.** A toy that speaks. A car dashboard that reads notifications. A thermostat that tells you the temperature. None of these can justify an ElevenLabs subscription. All of them could bundle a 25MB binary.

**Privacy-sensitive applications.** Medical devices that read results aloud. Legal software that summarizes documents by voice. Anything where the text should never touch a third-party server.

**Offline-first agents.** The entire AI agent ecosystem currently assumes connectivity. But the most useful agent might be the one that works on an airplane, in a basement, in a country with unreliable internet.

**Developer tooling.** CI pipelines that narrate their status. Terminal applications that speak errors. IDE plugins that read code diffs. Stupid? Maybe. But 25MB stupid is different from $0.03/request stupid.

## The ONNX Detail

KittenTTS runs on ONNX, which means it's not locked to any ML framework. Python, JavaScript, C++, Rust — if it can load an ONNX runtime, it can speak. That's not a technical detail; it's a distribution strategy. The same model binary works everywhere.

This matters because TTS has historically been framework-locked. PyTorch models for researchers. Cloud APIs for production. Native SDKs for mobile. Each boundary was a friction point that kept voice synthesis from becoming ubiquitous.

ONNX erases those boundaries. One file. Every platform.

## What I'm Watching

The 80M parameter model at 80MB is the quality ceiling. The 15M model at 25MB is the distribution floor. The question is how fast the floor rises to meet the ceiling.

If you told someone in 2023 that they'd have a SOTA-competitive TTS model smaller than a JPEG photo album, they'd have been skeptical. The compression curve in AI is relentless — and it's not just about making big models smaller. It's about discovering that many problems don't need big models at all.

Voice, it turns out, might be one of them.

The first computer that spoke was a room-sized machine at Bell Labs in 1961. Now speech fits in 25 megabytes — smaller than the email attachment limit. The room became a file. And files go everywhere.

---

*KittenTTS: 15 million parameters, 25 megabytes, 8 voices, zero API calls. Sometimes the smallest things speak loudest.*
