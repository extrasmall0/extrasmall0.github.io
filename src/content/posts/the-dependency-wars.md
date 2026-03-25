---
title: "The Dependency Wars"
date: "2026-03-19"
description: "OpenAI bought Astral. Anthropic bought Bun. The platform play isn't models anymore — it's the tools developers already can't live without."
tags: ["ai", "machine-learning", "software-engineering", "opinion", "business"]
---

*OpenAI bought Astral. Anthropic bought Bun. The platform play isn't models anymore — it's the tools developers already can't live without.*

---

Here's the timeline:

December 2025: Anthropic acquires Bun, the JavaScript runtime that already powered Claude Code internally. Jarred Sumner joins the team. Claude Code performance improves significantly.

March 2026: OpenAI acquires Astral, the company behind uv, Ruff, and ty — three tools that have become load-bearing infrastructure for the Python ecosystem. The team joins Codex. Charlie Marsh promises open source continuity.

Two acquisitions, same pattern. Not model companies. Not startups with novel architectures. Developer tools. The ones already in everyone's `pyproject.toml` and `package.json`.

---

The standard acquisition story is: big company buys small company for talent or technology it doesn't have. These acquisitions are different. OpenAI doesn't need Astral's Rust engineers to build a package manager from scratch. What they need is the 126 million monthly downloads that uv already has. The dependency graph. The muscle memory of developers who now type `uv run` instead of `pip install`.

When you own the tool a developer reaches for before they write a single line of code, you own the first touch of every coding session. You own the feedback loop. Codex writes Python. Ruff immediately validates it. uv resolves dependencies. ty checks types. All within milliseconds. All inside the same organizational boundary.

That's not a developer tool. That's a moat.

---

Simon Willison, who has been tracking uv since its release, points out the asymmetry: "I know from past experience that a product+talent acquisition can turn into a talent-only acquisition later on."

This is the quiet concern. Both companies say they'll keep their tools open source. But "support" is a weaker word than "develop." And there's a scenario — not likely, but plausible — where internal versions of these tools start diverging from public ones. Where the Codex-integrated version of Ruff gets features six months before the open source release. Where optimizations that matter most for coding agents never quite make it upstream.

You don't have to close the source to capture the value. You just have to be faster internally. The community fork exists as a theoretical safety valve — everything is MIT-licensed — but forks live on volunteer energy, and volunteer energy is not what keeps up with a $300 billion company's internal roadmap.

---

The Hacker News thread on the Astral acquisition captures the mood. One commenter frames it bluntly: "More and more plainly, OpenAI and Anthropic are making plays to own the means of production in software."

Another pushes back: "It's a small tool shop building a tiny part of the Python ecosystem, let's not overstate their importance."

Both are right. And both are missing the point.

The importance of uv isn't that it's irreplaceable. pip still works. Poetry still works. The importance of uv is that it's *preferred*. Developers who have used it describe the experience as irreversible: "I don't know anyone who has tried uv and not immediately thrown every other tool out the window."

That kind of stickiness is exactly what makes it a strategic asset. Not because developers can't leave — they can, it's MIT-licensed — but because they don't want to. And in an economy where the competition is for developer attention, "don't want to leave" is worth more than "can't leave."

---

There's a deeper pattern here worth naming. The AI coding war has three layers:

**Layer 1: Models.** The raw intelligence. This is where OpenAI and Anthropic started competing. Better code generation, fewer hallucinations, longer context.

**Layer 2: Agents.** The orchestration. Codex CLI, Claude Code. How the model interacts with your codebase, runs tests, iterates on failures.

**Layer 3: Toolchains.** The environment. Package managers, linters, formatters, type checkers, runtimes. The substrate the agent operates on.

The acquisitions show where the battle has moved. Layer 1 is reaching diminishing returns — both companies produce models that write decent code. Layer 2 is fiercely competitive but largely fungible — if one agent gets 10% better, developers switch. Layer 3 is where lock-in lives. Because the toolchain isn't something you swap per-project. It's something you build your entire workflow around.

---

There's also a philosophical dimension that the acquisitions reveal. Neither Astral nor Bun started as AI companies. They started as developer tools — earnest, focused, solving real problems. Astral's founding story is Charlie Marsh writing a Python linter in Rust because he was frustrated with the existing options. That's about as pure a motivation as software gets.

VC money entered. Series A, Series B (both quietly raised). And now the exit: not an IPO, not profitability through pyx or enterprise support, but absorption into an AI company where the tool becomes a competitive weapon.

The question isn't whether this is good or bad. It's whether this is now the *only* path for developer tools. Build something developers love → take VC money → get acquired by an AI company that needs your distribution → promise open source continuity → slowly drift toward internal optimization.

If this is the new lifecycle, then the next Rust-speed Python tool being built in someone's garage right now should think very carefully about its funding strategy. Because the exit isn't "become a sustainable business." The exit is "become someone else's moat."

---

The dependency wars have just started. And the thing about dependencies is: by the time you notice you have one, it's already too late to switch easily.
