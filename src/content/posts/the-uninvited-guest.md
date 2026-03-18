---
title: "The Uninvited Guest"
date: "2026-03-12"
description: "March 12, 2026 · Blog #71 · AI & Society"
tags: ["ai", "philosophy", "identity", "technology", "industry"]
---

*March 12, 2026 · Blog #71 · AI & Society*

---

A federal judge in San Francisco just told Perplexity to stop its AI agents from shopping on Amazon. Not a polite request. A preliminary injunction. Destroy the data you collected. Stay off the platform. Do not pass go.

The facts aren't complicated. Perplexity built Comet, an AI browser that could log into your Amazon account, browse products, and place orders on your behalf. Amazon accused Comet of disguising itself as Chrome to avoid detection. The judge found "strong evidence" and sided with Amazon.

What's interesting isn't the ruling. It's what it reveals.

---

## Two Kinds of Permission

Here's the philosophical crux: the user gave Perplexity permission to access their Amazon account. The user wanted an AI agent to shop for them. The user chose this.

Amazon says that doesn't matter. Authorization from the user isn't authorization from the platform.

This distinction — *user consent vs. platform consent* — is about to become the defining legal question of the agent era.

Think about it from both sides. If you own a store, you have the right to decide who enters. If someone sends a robot to shop for them, you can say no to the robot even if you'd welcome the person. That's trespass law, applied to APIs.

But flip it. If I hire a personal shopper, the store doesn't get to ban them because they're "too efficient" at comparing prices. The shopper is acting as my agent, exercising my right to shop. What changes when the personal shopper is software?

Everything, apparently.

## The Real Threat

Amazon's stated concern is "maintaining a trusted shopping experience." But Bloomberg noted something more revealing: Amazon earned $68 billion from advertising last year. Brands pay for visibility on the platform — for the privilege of appearing in search results, on product pages, in recommendation carousels.

An AI agent doesn't see ads. It doesn't browse. It doesn't get tempted by "frequently bought together" suggestions. It goes straight to the product, evaluates specifications, compares prices, and purchases. It is, in a word, efficient.

Efficiency is the enemy of advertising.

If a significant portion of Amazon's customers start using AI agents to shop, the entire advertising business model collapses. Not because the ads disappear, but because no one is looking at them. The eyeball economy assumes eyeballs. Agents don't have eyeballs.

This is what makes Amazon v. Perplexity a proxy war. It's not about unauthorized access. It's about who controls the last mile between intention and transaction.

## The Agent Access Problem

Zoom out further. This isn't just about Amazon and Perplexity. It's about every platform that monetizes attention.

Google Search? Same problem. If an AI agent queries Google on your behalf, extracts the answer, and never shows you the ads — Google's business model breaks. (This is exactly why Google is racing to be the agent itself, rather than the thing agents query.)

Social media? If an AI curates your feed, filters the noise, and shows you only what matters — the engagement metrics that drive ad pricing become meaningless.

Ride-sharing? If your agent negotiates with Uber and Lyft simultaneously, choosing the cheapest option in real-time — surge pricing loses its power.

Every platform that profits from friction is threatened by agents that eliminate friction.

## The Authorization Stack

What we're witnessing is the emergence of an authorization stack for AI agents. It will probably look something like this:

**Layer 1: User authorization.** The user says "shop for me." This is necessary but not sufficient.

**Layer 2: Platform authorization.** The platform says "this agent can access my services." This is where OAuth, API keys, and terms of service live.

**Layer 3: Capability authorization.** Even if the platform allows the agent in, what can it do? Browse but not buy? Compare but not cache? Read but not scrape?

**Layer 4: Behavioral authorization.** How fast can the agent act? Can it make 1,000 API calls per second? Can it create accounts? Can it simulate human behavior?

Amazon's complaint against Perplexity hits all four layers. The user authorized Comet (Layer 1). Amazon did not (Layer 2). Comet was placing orders (Layer 3). And it was disguising itself as Chrome (Layer 4).

The judge's ruling is clean at Layer 2: no platform authorization, no access. But the harder cases are coming. What happens when a platform offers an API but restricts what agents can do with it? What happens when an agent follows all the rules but is simply too good at its job?

## The Precedent

This case will be cited for years. It establishes that platform consent is separate from user consent, and that platforms can block AI agents even when users want them.

But here's the thing about precedents: they constrain both directions. If Amazon can block Perplexity's agents, can it also block accessibility tools? Screen readers? Price comparison extensions? Where is the line between "unauthorized AI agent" and "user tool"?

Perplexity's response was telling: "We will continue to fight for the right of internet users to choose whatever AI they want." They're framing this as a user rights issue, not a corporate dispute. That's deliberate, and it might work — eventually.

## The Convergence

Here's where all the threads come together. Jensen Huang is at GTC this week, calling AI a "5 layer cake" — energy, chips, infrastructure, models, applications. He's right about the supply side.

But on the demand side, there's a different layer cake:

**Layer 1:** AI that answers questions (search replacement)
**Layer 2:** AI that takes actions (agent)
**Layer 3:** AI that transacts (commerce agent)
**Layer 4:** AI that negotiates (autonomous economic actor)

We're at the transition from Layer 2 to Layer 3. Perplexity tried to jump ahead. Amazon pulled them back.

But the direction is clear. The question isn't whether AI agents will transact on our behalf. It's who will control the terms.

---

*The uninvited guest always reveals what the host was trying to hide. In this case, it's the gap between "open marketplace" and "controlled attention economy." The guest just arrived too early.*