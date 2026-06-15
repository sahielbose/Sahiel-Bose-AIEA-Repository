# Task 6: Deontic Logic Study

## Objective

Step back from implementation to study a formal system relevant to encoding
norms and obligations for reasoning agents. Deontic logic is the logic of
obligation, permission, and prohibition, and it is central to representing rules
that an explainable, accountable system must follow.

## Deliverable

`deontic_logic.md` is a written tutorial that covers:

- The three core operators: `O p` (obligatory), `P p` (permitted), and
  `F p` (forbidden).
- The duality relations among them, for example `P p` as `not O not p` and
  `F p` as `O not p`.
- How to write atomic and nested deontic rules.
- The modal axiom K and how it distributes obligation over implication to drive
  proofs.
- Contrary-to-duty obligations and the move to dyadic notation
  (`O (use_ashtray | smoke)`) to handle them.
- Consistency checking, where deriving both `O p` and `F p` signals a conflict
  that requires a rule change.

## Relevance to the lab

Obligation and prohibition are exactly the kinds of constraints an accountable
AI system must represent and respect. This task builds the conceptual vocabulary
for encoding such norms in the symbolic reasoners explored in the other tasks.
