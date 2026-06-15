# Task 3: Prolog Knowledge Base and Rule-Based Inference

## Objective

Build a hand-authored Prolog knowledge base and query it from Python, shifting
from generated logic (Task 2) to a curated, version-controlled knowledge base.
The focus is on rule-based inference: deriving facts that are never stated
explicitly.

## Files

- `family.pl` defines the domain. It contains parent facts of the form
  `parent(Parent, Child)`, sex facts (`male/1`, `female/1`), and a single rule
  that defines the grandparent relation:

  ```prolog
  grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
  ```

- `run_queries.py` loads the knowledge base with `pyswip` and queries
  `grandparent(X, Y)`, printing each derived pair.

## Key ideas

- The grandparent relation is **derived, not stored.** Prolog finds an
  intermediate `Z` such that `X` is a parent of `Z` and `Z` is a parent of `Y`,
  demonstrating resolution and backtracking over the fact base.
- A knowledge base maintained as source code is reproducible and reviewable,
  in contrast to facts produced ad hoc by a model.

## Running

```bash
python run_queries.py
```

Expected output lists every grandparent pair entailed by the facts, for example
that john and susan are grandparents of anna and james.

## Requirements

- Python 3.9 or newer
- `pyswip` and a local SWI-Prolog installation
