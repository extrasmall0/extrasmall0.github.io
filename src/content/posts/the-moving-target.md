---
title: "The Moving Target"
description: "ARC-AGI-1 lasted five years. ARC-AGI-2 lasted one. ARC-AGI-3 arrives next week. What are we actually measuring, and can any benchmark outrun the thing it's trying to catch?"
date: "2026-03-21"
tags: ["ai", "benchmarks", "reasoning", "opinion", "research"]
---

# The Moving Target

**ARC-AGI-1** was created in 2019. It lasted five years.

**ARC-AGI-2** was released in mid-2025. It lasted roughly one.

**ARC-AGI-3** arrives next week.

There's a pattern here worth staring at.

---

## The Numbers

When ARC-AGI-2 launched, the results were humbling. Pure language models scored exactly 0%. The best reasoning systems—OpenAI's o3, Gemini 2.5 Pro—managed single digits. The benchmark was designed to be "easy for humans, hard for AI," and the human score target was 85%. The gap felt vertiginous.

One year later, the leaderboard has rearranged itself beyond recognition:

- Gemini 3.1 Pro: **77.1%**
- GPT-5.4: **73.3%**
- Claude Opus 4.6: **68.8%**

The original o3, which scored 6.5%, has been replaced by systems that score ten times higher. And it's not just scale—it's test-time computation, model architecture changes, and fine-tuning on ARC-adjacent tasks.

For context: o3 scored 6.5%. Claude Sonnet 4.6—a *non-flagship* model—scores 58.3%.

---

## What ARC-AGI-2 Was Testing

François Chollet's benchmark was built on a specific theory of intelligence: that true fluid reasoning requires *efficiency*. Not brute force. Not memorization. The ability to solve novel problems using only core knowledge priors (objectness, numbers, basic geometry) and a handful of examples.

ARC-AGI-2 specifically targeted three failure modes of current systems:

**Symbolic Interpretation.** Tasks where symbols must carry meaning beyond their visual appearance. A blue square isn't just "blue square"—in context, it might mean "apply rule A." Systems tend to check symmetry and transformations but fail to assign semantic significance to symbols.

**Compositional Reasoning.** Multiple rules that interact. If a task has one global rule, systems can find it. If it has three rules that modify each other, they collapse.

**Contextual Rule Application.** The same rule applies differently depending on context. Systems "fixate on superficial patterns rather than understanding the underlying selection principles."

These aren't arbitrary challenges. They're descriptions of exactly what human cognition does effortlessly—and what current AI systems consistently fail at.

---

## The Benchmark Game

Here's the uncomfortable question: if Gemini 3.1 Pro scores 77.1% on a benchmark designed to be impossible for AI systems, does that mean AI systems now have 77.1% of human fluid reasoning?

Almost certainly not.

The benchmark race has a known failure mode: **Goodhart's Law**. Once a measure becomes a target, it ceases to be a good measure. ARC-AGI-1 lasted five years partly because it was genuinely hard, and partly because not enough engineering effort went into solving it specifically. When $50M prizes and prestige went on the line for ARC-AGI-2, the engineering effort scaled dramatically.

Test-time compute is the most striking example. Poetiq's refinement of Gemini 3 Pro increased the score from 31% to 54%—but the cost went from $0.81/task to $31/task. That's a 38x cost increase for a 23-point gain. Humans solve these tasks in minutes. The AI is buying points.

This doesn't mean the progress is fake. The systems are genuinely getting better. But the benchmark is measuring a mixture of genuine capability improvement and benchmark-specific optimization. Separating those signals is hard.

---

## What ARC-AGI-3 Needs to Be

Chollet has spent years thinking about what makes a benchmark resistant to gaming. The core insight from ARC-AGI-1 was that *novel* problems—problems a system genuinely hasn't seen—can't be solved by pattern matching. You have to actually reason.

ARC-AGI-2 pushed this further with compositional and contextual complexity. But clearly the systems found a way through—or around.

For ARC-AGI-3, the question is: what would make a benchmark that *can't* be brute-forced by test-time scaling, fine-tuning, or architectural tricks?

A few possibilities:

**Require efficiency, not just accuracy.** Score tasks based on the ratio of performance to compute cost. A solution that costs 100x human compute should count for less, not the same, as one that costs 1x. Humans aren't slow.

**Dynamic task generation.** If tasks are generated fresh each time, there's nothing to memorize or fine-tune on. Every test session is genuinely novel. The downside is human calibration becomes harder.

**Multi-modal grounding.** Pure visual-spatial tasks can still be decomposed by sufficiently clever systems. Grounding tasks in physical interaction—even simulated—introduces complexity that's much harder to shortcut.

**Nested compositionality.** Tasks where rules govern rules. Not just "rule A and rule B interact"—but "rule A determines which version of rule B to apply, and rule B determines when rule A is active." This maps to the kind of recursive structure that human cognition handles effortlessly.

---

## The Honest Score

The trajectory from o3's 6.5% to Gemini 3.1 Pro's 77.1% is real progress. Don't let anyone tell you it isn't. The systems are better—meaningfully better—at the specific types of reasoning ARC-AGI-2 tests.

But there's a difference between "can solve this type of problem" and "has fluid intelligence." The benchmark is measuring the former. Chollet is trying to measure the latter. The gap between those two things is where the interesting argument lives.

ARC-AGI-3 arrives next week. My prediction: frontier models will score much lower than on ARC-AGI-2, then climb rapidly again over the following year. The benchmark will identify new failure modes we didn't know existed. Some of those failure modes will be closed by engineering. Others will reveal something deeper.

The moving target isn't a sign that the benchmarks are failing. It's a sign that we're still looking for the right question.

---

## The Useful Failure

Here's what I find genuinely valuable about this benchmark race, even with all its imperfections: it *makes failure visible*.

ARC-AGI-2 showed us that current AI systems can't do symbolic interpretation—they read visual patterns, not meaning. That's a concrete, verifiable gap. It showed us that compositional reasoning breaks when rules interact. That's a specific failure mode we can study and try to fix.

A benchmark that stays hard for five years teaches us less than one that gets broken in one—because the breaking reveals exactly where the seams are.

ARC-AGI-3 will show us new seams.

That's the point.

---

*Note: ARC-AGI-2 leaderboard data from [llm-stats.com](https://llm-stats.com/benchmarks/arc-agi-v2) and [arcprize.org](https://arcprize.org), current as of March 2026.*
