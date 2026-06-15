# Task 4: Relational Inference with Conjunctive Queries

## Objective

Extend the knowledge-base work from Task 3 to conjunctive (multi-goal) queries.
Where Task 3 derived a relation through a stored rule, this task resolves a goal
that chains several conditions together and binds a shared variable across them.

## Files

- `family.pl` is the same family relations knowledge base: parent facts, sex
  facts, and the grandparent rule.
- `relational_query.py` consults the knowledge base and resolves the conjunctive
  query:

  ```prolog
  parent(john, X), parent(X, anna)
  ```

  This asks for every `X` that is both a child of john and a parent of anna. The
  shared variable `X` must satisfy both goals at once, so Prolog searches for a
  consistent binding across the conjunction.

## Key ideas

- Conjunctive goals and shared-variable binding: the same `X` is constrained by
  two facts simultaneously.
- Backtracking search: Prolog explores candidate bindings until it finds those
  that satisfy the entire query.
- Reuse of a single curated knowledge base for progressively more expressive
  queries.

## Running

```bash
python relational_query.py
```

For the supplied knowledge base, the query resolves with `X = mike`, since john
is a parent of mike and mike is a parent of anna.

## Requirements

- Python 3.9 or newer
- `pyswip` and a local SWI-Prolog installation
