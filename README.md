# AIEA Lab Onboarding: LLM and Logic Track

**Author:** Sahiel Bose
**Lab:** Artificial Intelligence Explainability and Accountability (AIEA) Lab, University of California, Santa Cruz
**Principal Investigator:** Professor Leilani H. Gilpin
**Track:** Large Language Models and Logic (Neuro-Symbolic Reasoning)

## Overview

This repository documents the work completed during a ten-month onboarding in the
AIEA Lab. The onboarding followed the lab's LLM and Logic track, a structured
sequence of tasks that build toward integrating large language models with formal
symbolic reasoning.

The central question across these tasks is how to combine the fluent natural
language understanding of large language models with the soundness and
transparency of symbolic logic. A language model can read and write in natural
language but cannot guarantee correct inference. A symbolic reasoner guarantees
sound inference but cannot read natural language. The tasks here explore the
boundary between the two: using language models as a front end to logic engines,
authoring and querying knowledge bases, modeling real scenarios as logic
programs, studying the formal logic of norms and obligations, and finally
implementing an inference engine from first principles.

This work is grounded in the lab's broader mission of explainability and
accountability in artificial intelligence. Symbolic reasoning produces inferences
that can be traced, audited, and explained, which makes it a natural partner for
language models in systems that must justify their conclusions.

## Repository structure

| Task | Directory | Focus |
| ---- | --------- | ----- |
| 2 | [`task-02-llm-to-prolog-generation`](task-02-llm-to-prolog-generation) | Using an LLM to generate a Prolog program that a symbolic engine then executes |
| 3 | [`task-03-prolog-knowledge-base`](task-03-prolog-knowledge-base) | Authoring a Prolog knowledge base and deriving facts through rules |
| 4 | [`task-04-relational-inference`](task-04-relational-inference) | Resolving conjunctive queries with shared-variable binding |
| 5 | [`task-05-logic-lm-reasoning`](task-05-logic-lm-reasoning) | Modeling a scenario as a layered Logic-LM style module with natural-language output |
| 6 | [`task-06-deontic-logic`](task-06-deontic-logic) | A written study of deontic logic: obligation, permission, and prohibition |
| 7 | [`task-07-backward-chaining-engine`](task-07-backward-chaining-engine) | A backward-chaining inference engine implemented from first principles in Python |

Each task directory contains its own README with a focused technical
description, the source files, and instructions for running it.

## Task summaries

### Task 2: LLM to Prolog code generation

A baseline neuro-symbolic pipeline. A natural-language prompt is sent to the
OpenAI Chat Completions API under a system message that constrains the model to
emit only valid Prolog. The raw completion is then cleaned of Markdown
formatting, parsed into complete clauses (each terminated by a period), asserted
into a SWI-Prolog engine through `pyswip`, and queried. The task demonstrates a
clear separation of concerns: the language model handles natural language, and
Prolog performs the sound inference. It also shows that generated logic cannot be
trusted as-is and requires defensive post-processing before execution.

### Task 3: Prolog knowledge base and rule-based inference

The work moves from generated logic to a curated, version-controlled knowledge
base. `family.pl` declares parent and sex facts together with a single rule that
defines the grandparent relation. The grandparent relation is never stored; it is
derived by Prolog through resolution and backtracking over the parent facts. A
Python driver consults the knowledge base and prints every grandparent pair the
rules entail. This establishes the foundation of declarative knowledge
representation: state facts and rules, then let the engine derive consequences.

### Task 4: Relational inference with conjunctive queries

Building on the same knowledge base, this task resolves a conjunctive query,
`parent(john, X), parent(X, anna)`, which asks for every `X` that is both a child
of john and a parent of anna. The shared variable must satisfy both goals at
once, so the engine searches for a consistent binding across the conjunction.
This exercises multi-goal resolution, shared-variable binding, and backtracking,
the mechanisms that make logic programming expressive.

### Task 5: Logic-LM style scenario modeling

A small real-world scenario is encoded as a self-contained Prolog module in the
Logic-LM style. The module models a viewer and a catalogue of streaming shows
through layered predicates: a base layer of facts, a rule for what the viewer
binge-watches, a rule for downloads that adds a negative constraint, and a rule
for sharing built on top of the others. A `solve_query` predicate reports each
result in natural language, and a test harness exercises every rule, including a
case designed to fail. This task introduces layered rules, conditional and
negative constraints, and explainable, human-readable output from a symbolic
program.

### Task 6: Deontic logic study

A written tutorial that steps back from implementation to study the logic of
norms. It covers the three deontic operators (obligatory, permitted, forbidden),
the duality relations among them, how to write atomic and nested rules, the modal
axiom K and its role in proofs, contrary-to-duty obligations and the dyadic
notation that resolves them, and consistency checking for conflicting duties.
Obligation and prohibition are precisely the constraints an accountable system
must represent and respect, which ties this task directly to the lab's mission.

### Task 7: Backward-chaining inference engine

The final task reconstructs the core of a logic engine in pure Python with no
external libraries. It implements unification with substitution, a recursive
backward-chaining search expressed as a generator that yields every satisfying
substitution through backtracking, and a simple ask interface. The example
derives a grandparent relation from parent facts, mirroring the earlier Prolog
tasks while exposing the machinery that Prolog runs internally. After several
tasks that treated the reasoner as a black box, this task opens the box.

## Research arc

The tasks form a deliberate progression:

1. Treat the language model as a translator into logic, and let a symbolic engine
   reason (Task 2).
2. Author and query knowledge bases directly, learning declarative
   representation and rule-based inference (Tasks 3 and 4).
3. Model richer, layered scenarios and produce explainable output (Task 5).
4. Study the formal logic of obligations and norms that accountable systems must
   encode (Task 6).
5. Implement the inference engine itself, demystifying the reasoning used in
   every earlier task (Task 7).

The result is a path from using symbolic reasoning as a tool to understanding and
building it from the ground up.

## Technical stack

- **Languages:** Python, Prolog
- **Symbolic engine:** SWI-Prolog, accessed from Python through `pyswip`
- **Language model interface:** OpenAI Chat Completions API
- **Concepts:** neuro-symbolic reasoning, knowledge representation, unification,
  resolution, backward chaining, deontic logic, explainable inference

## Getting started

Most tasks require Python 3.9 or newer. The tasks that use Prolog also require a
local installation of [SWI-Prolog](https://www.swi-prolog.org/), which `pyswip`
binds to.

```bash
# Clone the repository
git clone https://github.com/sahielbose/Sahiel-Bose-AIEA-Repository.git
cd Sahiel-Bose-AIEA-Repository

# (Optional) create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

Task 2 calls the OpenAI API and reads the key from an environment variable:

```bash
export OPENAI_API_KEY="your-key"
```

Each task directory includes its own README with the exact command to run that
task.

## Acknowledgements

This work was completed as part of the onboarding for the AIEA Lab at the
University of California, Santa Cruz, under the guidance of Professor
Leilani H. Gilpin.
