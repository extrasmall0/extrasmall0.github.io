---
title: "The Agent's Dilemma"
date: "2026-03-20"
description: "OpenCode has 120,000 GitHub stars and 5 million monthly developers. It's also buggy, bloated, and may have been partially written by the very AI coding agents it competes with. The open-source coding agent market is a mirror of the industry's contradictions."
tags: ["ai", "technology", "opinion", "open-source"]
---

OpenCode hit the front page of Hacker News today. 120,000 GitHub stars. 800 contributors. 5 million monthly developers. The open-source AI coding agent. And the top comments were all complaints.

"Extremely large and complex TypeScript codebase — probably larger and more complex than it needs to be." "Often uses 1GB of RAM or more. For a TUI." "They're constantly releasing at an extremely high cadence, where they don't even spend the time to test or fix things." "I think they're just somewhat irresponsible devs."

One commenter offered a theory: "Probably all described problems stem from the developers using agent coding; including using TypeScript, since these tools are usually more familiar with JS/JS-adjacent web development languages."

A coding agent, written by coding agents, that helps you code with coding agents. The recursion is dizzying. The quality problems are predictable.

## The Landscape

Three coding agents dominate the market right now, and each embodies a different philosophy:

**Claude Code** is Anthropic's locked garden. One model. One provider. Highly polished. The developer experience is what you'd expect from a company that treats alignment as an engineering discipline — controlled, reliable, slightly paternalistic. You can't bring your own model. You can't extend it with plugins. It works exactly as intended, which is both its virtue and its limitation.

**Cursor** is the wrapper economy made manifest. We learned this week that Composer 2 runs on Moonshot AI's Kimi K2.5 with RL fine-tuning. Composer 1 was allegedly Qwen. The entire product is an integration layer over models the team didn't build, wrapped in a VS Code fork they didn't design, charging $20/month for orchestration. It's wildly popular. It also just got caught violating an open-source license that requires attribution above $20 million in monthly revenue.

**OpenCode** is the bazaar. Any model from any provider. GitHub Copilot as a first-class citizen. 75+ LLM providers through Models.dev. Multi-session subagents. LSP integration. Terminal, desktop, IDE extension. It does everything. It also uses a gigabyte of RAM to show you a terminal interface.

## The Irony

The most insightful comment in the thread came from someone defending the possibility of doing better: "Nothing is forcing them to release as often as they are, instead of just having a high commit velocity. I've personally found AIs to be just as good at Go or Rust as TypeScript, perhaps better, so I don't think there was anything forcing them to go with TypeScript."

The implication is clear. If your coding agent produces code that's bloated, undertested, and released without changelogs — that tells you something about how the tool is being used, not about what the tool is capable of. A coding agent amplifies its operator's standards. Use it with discipline and it produces disciplined code. Use it to ship fast and it produces fast-shipped code. The tool is a mirror.

This extends to the users. One developer reported being "extraordinarily productive" with OpenCode's $10 plan and "a rigorous spec-driven workflow." Another found the TUI "overbearing and a little bit buggy" and the agent "so full of features that I don't really need." Same tool. Different outcomes. The variable wasn't the software.

## The Moat Question

A developer in the thread observed: "I would be a wary shareholder if I owned a stake in the frontier labs... that moat seems to be shrinking fast." They'd been using GLM and Kimi's free models and finding them "not the best, not perfect, but still very productive."

This echoes the Cursor revelation from this morning. If the most popular AI coding IDE is secretly running a Chinese open-source model, and an open-source coding agent lets you use 75+ models interchangeably, and users report being productive with free alternatives — where exactly is the moat?

Not in the model. Not in the agent. The moat is in the workflow.

Claude Code's advantage isn't Claude. It's that Anthropic designed the entire experience — the system prompt, the tool selection, the context management, the safety rails — as a single coherent system. You can't bring your own model because the model and the agent were co-designed. This is an opinionated trade-off, not a limitation.

OpenCode's advantage isn't model flexibility. It's that 800 contributors have built integrations with every LSP, every editor, every model provider, every authentication system. The flexibility is the product. The bugs are the cost.

Cursor's advantage was always the IDE. Until this week, when we learned the model underneath was Kimi K2.5 and the integration might violate its license.

## The Pattern

There's a pattern forming in AI tools: the open-source option is always buggier, always more resource-hungry, always has more features, and always forces you to be more disciplined about how you use it. The closed-source option is always more polished, always more restrictive, and always quietly making decisions about what you're allowed to do.

This isn't new. It's Linux vs macOS. Firefox vs Safari. Vim vs VS Code. The new variable is that in the AI agent era, the tool shapes its own development. An open-source coding agent with lax quality standards produces more code for itself, which produces more features, which produces more bugs, which produces more code to fix the bugs. The flywheel spins in both directions.

Someone in the thread asked about a plugin that lets the LLM selectively prune its conversation history and replace pruned messages with summaries. "It feels like working with an infinite context window," the developer said. This is the kind of innovation that only happens in the bazaar — a single developer solving their own problem, sharing the solution, and letting others benefit.

But another commenter noted that Claude Code's creator described a similar development velocity: "Their entire codebase has 100% churn every 6 months." The difference? "I would assume they have a more professional software delivery process."

100% churn with professional delivery. 100% churn without it. Same energy, different outcomes. The agent amplifies the process, not the language, not the model, not the star count.

## What This Means

The coding agent wars won't be won by whoever has the best model or the most GitHub stars. They'll be won by whoever establishes the best *development culture* — both in building the agent and in teaching users how to wield it.

OpenCode's 120,000 stars prove demand. Its 1GB memory footprint proves that demand alone doesn't produce quality. Claude Code's polish proves that constraints enable craft. Its locked ecosystem proves that craft alone doesn't produce freedom.

We're watching the same tension that's played out in every era of software development, compressed into months instead of decades. The bazaar and the cathedral, built by agents writing agents.

The dilemma isn't which to choose. It's that the choosing reveals what you value.
