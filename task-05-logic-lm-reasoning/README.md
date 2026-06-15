# Task 5: Logic-LM Style Scenario Modeling

## Objective

Model a small real-world scenario as a self-contained Prolog module in the
Logic-LM style, where natural-language statements about a situation are
translated into facts and rules and then checked by symbolic queries. This moves
beyond family relations to a domain with layered, conditional rules.

## File

`logic_lm.pl` defines a module `logic_lm` that exposes three predicates:
`binge_watches/2`, `downloads/2`, and `shares/3`. The scenario concerns a viewer
named karen and a catalogue of streaming shows.

The module is organized in layers:

- **Facts.** A catalogue of shows (`netflix_show/1`) and a subset marked
  `popular/1`.
- **Rules.**
  - `binge_watches(karen, Show)` holds when `Show` is both a show and popular.
  - `downloads(karen, Show)` builds on the rule above and adds the condition
    that the show is not `black_mirror`, demonstrating negative constraints
    through `\=`.
  - `shares(karen, Show, lisa)` holds for any show karen binge-watches.
- **Explanation.** `solve_query/1` calls a goal and prints whether it succeeded
  or failed in natural language, giving the symbolic result a readable form.
- **Test harness.** `test_queries/0` runs a representative set of queries that
  exercise each rule, including a case that is expected to fail.

## Key ideas

- Layered rules where higher-level predicates are defined in terms of
  lower-level ones.
- Conditional and negative constraints (`Show \= black_mirror`).
- Reporting results in natural language, a step toward explainable symbolic
  reasoning.

## Running

Load the module in SWI-Prolog and run the test harness:

```bash
swipl -g test_queries -t halt logic_lm.pl
```

## Requirements

- SWI-Prolog
