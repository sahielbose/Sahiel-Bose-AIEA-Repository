# Task 7: Backward-Chaining Inference Engine

## Objective

Implement a first-order inference engine from first principles in pure Python,
with no external logic library. Earlier tasks treated Prolog as a black box;
this task reconstructs the core of that black box to show exactly how resolution
and unification work.

## File

`backward_chaining.py` implements the full pipeline in four small functions:

- `is_var(x)` identifies variables, which are strings beginning with `?`.
- `substitute(exp, subs)` applies a substitution recursively to a term, following
  chains of bindings until no variable can be replaced further.
- `unify(x, y, subs)` finds a substitution that makes two terms equal. It handles
  variable-to-term binding in either direction and recurses structurally over
  tuples of equal length, returning `None` when no unifier exists.
- `bc(kb, goals, subs)` is the backward-chaining search. It proves a list of
  goals against the knowledge base by unifying the first goal with each clause
  head and recursively proving that clause's body followed by the remaining
  goals. It is written as a generator, so it yields every satisfying
  substitution through backtracking.
- `ask(kb, query)` collects all solutions for a single query.

Terms are tuples and clauses are `(head, body)` pairs, where `body` is a list of
sub-goals. A fact is simply a clause with an empty body.

## Example

The script encodes parent facts and a grandparent rule, then asks
`("Grandparent", "John", "?who")`. The engine derives that John is a grandparent
of Susan by unifying the query with the grandparent rule and proving the two
parent sub-goals.

## Key ideas

- Unification as the core operation of logic programming.
- Substitution composition and the resolution of variable chains.
- Backward chaining as a depth-first, generator-driven search with backtracking.
- A complete, dependency-free reimplementation of the inference that Prolog
  performs internally.

## Running

```bash
python backward_chaining.py
```

## Requirements

- Python 3.9 or newer (standard library only)
