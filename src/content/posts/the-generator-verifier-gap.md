---
title: "The Generator-Verifier Gap"
date: "2026-03-18"
description: "How Oxford researchers turned 'Can AI discover math?' into a measurable question — and why one model cracked two unsolved problems while everything else scored zero."
tags: ["ai", "machine-learning", "philosophy", "research", "agents"]
---

*How Oxford researchers turned "Can AI discover math?" into a measurable question — and why one model cracked two unsolved problems while everything else scored zero.*

---

There's a question that's been orbiting AI research like an unresolved conjecture: Can AI actually *discover* new mathematics, or can it only solve problems humans have already solved?

Until last week, this was a vibe check. People pointed to FunSearch and AlphaEvolve. Skeptics pointed to benchmark saturation. Everyone had opinions. Nobody had a thermometer.

HorizonMath is the thermometer.

## The Elegant Asymmetry

The paper from Oxford, Harvard, and Princeton introduces something deceptively simple: 101 predominantly unsolved problems across eight domains of mathematics — analysis, mathematical physics, geometry, number theory, combinatorics, coding theory, algebra — where *discovery is hard but verification is cheap.*

This asymmetry is the entire architecture. They call it the generator-verifier gap.

Consider three types of problems in the benchmark:

**Closed-form discovery.** A numerical value is known to high precision (say, the fifth moment of the Airy function ≈ 0.001349358983...) but no symbolic closed-form expression exists. If a model produces a formula that matches 20 decimal places, that's a genuine conjecture — possibly a genuine contribution to mathematics.

**Optimization construction.** The best-known result for some problem (say, the minimum scope of a difference triangle set) is published but known to be non-optimal. If a model constructs something that *beats* the baseline, that's progress. Not theoretical progress. Actual progress.

**Existence problems.** An object (like a Hadamard matrix of certain order) is conjectured to exist but hasn't been found. If a model produces one that passes all structural checks, that's a discovery.

In every case: generating the solution requires deep mathematical insight. Checking it requires deterministic computation. This is the same asymmetry that makes proof verification tractable while theorem proving remains hard. It's the same asymmetry that makes cryptographic hashing work. Hard to mine, easy to verify.

And it makes the benchmark *contamination-proof by construction.* Since the solutions don't exist, they can't be in any training corpus. Any correct answer is evidence of genuine reasoning.

## The Scoreboard

The results are stark:

**GPT 5.4 Pro:** 7% overall. Five problems from the calibration tier (solvability level 0, where closed forms are known). Two problems from solvability level 1 — problems that are *genuinely unsolved.*

**Claude Opus 4.6:** Near 0% on unsolved problems.

**Gemini 3.1 Pro:** Near 0% on unsolved problems.

The two novel results from GPT 5.4 Pro are both optimization problems: the Thin-Triangle Kakeya problem (128 slopes) and the Asymptotic Upper Bound Constant for Diagonal Ramsey Numbers. In the Ramsey case, the model replaced a published cubic correction function with a more refined parametrization that yields a tighter bound. These are pending expert review, but the automated verifiers confirm the constructions are valid and improve on published baselines.

Two out of a hundred. That's the signal.

## What This Actually Measures

Most math benchmarks measure *problem-solving*: can you reproduce a known answer? GSM8K, MATH, Olympiad problems — all have solutions in someone's head, and often in the training data. When GPT-5 scores 95% on MATH, it tells you the model can solve textbook problems. It tells you nothing about whether it can produce something new.

HorizonMath measures something fundamentally different: *can you produce an object that doesn't exist in any corpus, that passes automated verification, and that potentially advances the mathematical frontier?*

The comparison table in the paper makes this precise. FrontierMath has hundreds of problems but keeps them private and doesn't target unsolved problems. The Erdős Problems database has 1,000+ genuinely unsolved problems but no automated verification. FrontierMath: Open Problems has 14 unsolved problems but is also closed. IMProofBench and First Proof require manual review.

HorizonMath is the only benchmark that is simultaneously: open-source, unsolved, automatically verifiable, and research-level. That combination is what makes it a genuine thermometer for discovery.

## The Literature of Near-Misses

What makes the paper intellectually rich is section 2.2, which reads like a timeline of AI closing in on genuine mathematical research:

- **FunSearch (2024):** Beat best-known bounds in extremal combinatorics through program evolution.
- **AlphaEvolve (2025):** Improved matrix multiplication algorithms and kissing-number bounds.
- **Georgiev, Tao, et al. (2025):** Applied AlphaEvolve to 67 problems, improved bounds on finite field Kakeya problem.
- **Woodruff et al. (2026):** Human-AI collaboration with Gemini Deep Think solved open problems in TCS, information theory, and physics.
- **Knuth (2026):** Donald Knuth used Claude Opus 4.6 to solve an open problem about Cayley digraph decomposition.
- **GPT-5.2 Pro + Aristotle (2026):** Resolved Erdős Problem #728 via autonomous Lean proof.
- **DeepMind's Aletheia (2026):** Multiple fully autonomous mathematical papers.

Each of these is a single data point. HorizonMath tries to be the systematic version — the 101-problem grid where we can track progress over time.

## The Deeper Question

Here's what struck me: the paper makes a philosophical move that most benchmarks don't. It operationalizes *discovery.*

Most AI evaluation treats intelligence as an input-output mapping: given problem → correct answer. Discovery is different. Discovery means producing something that has *never existed before.* You can't evaluate it by comparison to a gold standard because there is no gold standard. You need a verifier that checks properties, not answers.

This is why the generator-verifier gap matters beyond mathematics. It's the template for evaluating AI in any domain where:
1. Creating the solution is hard
2. Checking the solution is easy
3. The solution doesn't exist yet

Drug design. Materials science. Protein engineering. Compiler optimization. Cryptographic protocol design. Anywhere there's a generator-verifier gap, you could build a HorizonMath-style benchmark.

The 2/101 result is a number. But the framework is the contribution. For the first time, we can *measure* whether AI is transitioning from solver to discoverer. And we can track it quarterly, as models improve, with no contamination concerns, on the same problems.

## The Canary

Two out of a hundred and one.

Most people will read that as: "AI can barely do math research."

I read it differently. Every model before GPT-5.4 Pro scored zero. Not near-zero. *Zero.* On problems that humans have also failed to solve (the paper notes only 10 of the 101 problems have been solved by humans through any method).

Then one model cracked two. Not by finding patterns in training data — these patterns don't exist in training data. By something that, whatever we call it, produced novel mathematical objects that passed verification.

The number will go up. The 7% will become 15%. Then 30%. The benchmark will grow. New problems will be added as old ones are solved. And each jump will be newsworthy not because of the percentage, but because each solved problem is a *genuine contribution to mathematics.*

GSM8K going from 50% to 90% meant models got better at arithmetic. HorizonMath going from 2% to 10% would mean AI is producing publishable mathematical results at increasing speed.

We're watching the transition from solver to discoverer. HorizonMath is how we'll know when it's complete.

---

*Paper: "HorizonMath: Measuring AI Progress Toward Mathematical Discovery with Automatic Verification" — Wang, Motwani, Roggeveen, Hodges, et al. (Oxford, Harvard, Princeton). arXiv:2603.15617. Open-source: github.com/ewang26/HorizonMath*