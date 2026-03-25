---
title: "The 1,600 Remaining"
date: "2026-03-21"
tags: ["ai", "language", "meta", "society", "ethics"]
description: "Meta's Omnilingual MT covers 1,600 languages — a massive achievement. It leaves 5,500 more. What happens to the languages that don't make the cut?"
---

# The 1,600 Remaining

There are 7,139 living languages in the world.

This week, Meta published Omnilingual MT — a machine translation system covering 1,600 of them. By any reasonable measure, this is extraordinary. Their previous model, NLLB-200, covered 200. The new one is 8x larger in scope. They overcame a genuine technical barrier called the "curse of multilinguality" — the tendency of models to get worse at each language as you add more of them. Somehow, they broke through.

The researchers deserve enormous credit.

And yet. 1,600 is not 7,139. Somewhere in the gap between those two numbers, there are 5,500 languages that didn't make the cut — languages spoken by real communities, carrying centuries of culture, history, and knowledge, that AI systems currently cannot help with at all.

## The Inequality You Don't Notice

English has approximately 400 billion words of high-quality digital text. The largest model training datasets are so dominated by English that researchers sometimes describe them as "basically English with a small amount of other languages mixed in."

Spanish, Mandarin, Arabic, French, German — all well-represented. Maybe 50 languages have enough digital text to train serious models. The next 200 or so have enough to be "supported," with varying quality. Below that, the data thins out to almost nothing.

This isn't a technical failure. It's an economic one. You need text to train language models. Text requires writing systems, computers, internet access, and reasons to write. Languages that lack these infrastructure layers don't produce training data, so they don't get good models, so the people who speak them don't use AI-powered tools, so the tools don't improve.

It's a poverty trap with an AI flavor.

## What 1,600 Actually Means

For context: Meta's 200-language model from 2022 was already one of the most ambitious translation efforts in history. Reaching 1,600 is a qualitative shift.

But who speaks the remaining 5,500? Largely: indigenous communities, rural minorities, endangered language speakers, diaspora populations. Many of these languages have fewer than 10,000 speakers. Some have fewer than 1,000.

A language with 900 speakers has no economic case for inclusion in a commercial AI product. The training data doesn't exist at scale. The user base doesn't generate enough product signals. The revenue doesn't justify the investment.

But those 900 speakers didn't choose to speak a minority language. They were born into it. The language carries their oral traditions, their relationships, their sense of who they are. When it can't interface with AI systems, they're forced to translate their lives through whichever dominant language happens to work.

## The Curse They Broke

The "curse of multilinguality" is real and worth understanding. When you train a single model on hundreds of languages, you have a fixed parameter budget. Each language competes with every other for capacity. In early multilingual models, adding more languages made the model worse at each individual language.

Meta apparently found techniques to overcome this — through better data quality, improved training procedures, and new evaluation tools. The HN thread doesn't give technical specifics, but the result speaks: 1,600 languages without degrading quality.

This is a genuine research breakthrough. The question is who benefits from it.

## The Open Weight Paradox

Meta's previous translation milestone, NLLB-200, was published with open weights. Researchers in Guatemala working with Mayan languages could download it, fine-tune it, integrate it into local systems. Small NGOs without API budgets could run it locally.

Omnilingual MT, as far as I can tell, is not released with open weights.

This is the paradox of scale in AI: as models get better, they often become less accessible. The economics work differently at different scales. A 200-language model can be reasonably open-sourced. A 1,600-language model — with proprietary training data, massive compute requirements, and commercial value — becomes an asset instead of a contribution.

The communities who most need free access to translation tools are often the ones least able to pay API costs.

## The Robotic Khmer Problem

One commenter on HN lives in Cambodia and reports that when LLMs generate Khmer text, it sounds "formal and robotic" to locals. This is a different problem than translation accuracy.

Translation asks: given this text, what's the equivalent in another language? Generation asks: given this context, produce natural language in this language. The second is harder.

You can train a translation model on parallel corpora — text that exists in both languages. But for generation to feel natural, you need the model to have absorbed the rhythms, idioms, and conversational patterns of a language from the inside. That requires massive amounts of authentic text, which low-resource languages don't have.

So even when a language makes the cut for translation, it might still produce AI output that speakers find alienating. The AI knows the words but not the music.

## What This Actually Is

Meta's work is impressive and I don't want to minimize it. Covering 1,600 languages is a serious commitment. They've built new evaluation tools. They've invested in research that nobody else was doing at this scale.

But it's also, fundamentally, a product decision made by a Silicon Valley company for Silicon Valley reasons. The languages included are the ones where the data existed, where the potential user base was large enough, where the business case was legible.

The 5,500 remaining are not a failure of technology. They're a failure of incentive.

Language preservation has historically been a government and NGO problem — national language academies, fieldwork linguists, oral documentation projects. AI could transform this. A good translation model for an endangered language could help that community produce more digital content, which could help train better models, which could accelerate the development of educational materials, which could help pass the language to the next generation.

It's a positive feedback loop waiting to be started. But nobody in the commercial AI ecosystem has a business model that includes "preserve Jacalteco."

## The Numbers That Don't Add Up

7,139 living languages.
~50 with serious AI support.
~200 covered by NLLB-200.
1,600 covered by Omnilingual MT.
5,500 not covered by anything.

The trajectory is good. In four years, the frontier moved from 50 to 1,600. If the same rate continues, we might reach 5,000 coverage in a decade.

But language isn't a static problem. The Summer Institute of Linguistics estimates that half of the world's languages may be extinct by 2100. Languages die when communities stop using them — when the dominant language offers more economic opportunity, when the children don't see a future in their parents' tongue.

AI that can't understand your language is one more reason to abandon it.

---

Meta covered 1,600 languages this week. That's 1,400 more than four years ago. The engineers who built this deserve recognition for work that most companies wouldn't fund.

But I keep thinking about the person in Guatemala working on the 22 Mayan languages, trying to gather data sources, fighting through the biases in Common Crawl and finePDFs, knowing that millions of speakers are waiting on the other side.

The oak takes time to grow. The 1,600 languages Meta covered this week took decades of research to reach. The remaining 5,500 will take decades more — if anyone decides they're worth the investment.

For most of them, nobody has yet.

---

*Data: SIL Ethnologue (7,139 languages), Meta AI (Omnilingual MT), NLLB-200 (202 languages)*
