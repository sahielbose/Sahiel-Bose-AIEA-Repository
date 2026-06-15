# An Introduction to Deontic Logic

**Author:** Sahiel Bose
**Date:** April 9, 2025

## Overview

Deontic logic is a way to write rules with symbols instead of long sentences.
Instead of reasoning only about what is true or false, it reasons about what
must happen, what may happen, and what is not allowed. Three operators carry
most of the meaning:

- `O p` means "p is obligatory."
- `P p` means "p is permitted."
- `F p` means "p is forbidden."

## Duality of the operators

The three operators are related to one another. Something is permitted exactly
when its opposite is not obligatory, so `P p` is equivalent to `not O not p`.
Something is forbidden exactly when its opposite is obligatory, so `F p` is
equivalent to `O not p`. These equivalences let any one operator be expressed in
terms of the others.

## Writing rules

Once the operators are fixed, rules are written the same way as plain logic
sentences, with each clause placed under `O`, `P`, or `F`. For example:

- `O (clean_room)` says the room has to be cleaned.
- `P (play_games)` says playing games is allowed.
- `O (clean_room -> watch_TV)` says that watching TV is required whenever the
  room is cleaned.

Short, descriptive propositions such as `clean_room`, `pay_tax`, and `eat_food`
keep the rule set readable.

## Reasoning with axiom K

Deontic logic inherits the standard modal axiom K: if `O (p -> q)` holds and
`O p` holds, then `O q` follows. In practice, if driving is obligatory and "if
you drive you must buckle up" is obligatory, then buckling up is obligatory.
Axiom K is the distributivity of obligation over implication, and it powers most
everyday proofs. Tools such as Prolog or SMT solvers can apply the rule
automatically, so the symbols do not have to be manipulated by hand.

## Contrary-to-duty obligations

Standard deontic logic struggles with contrary-to-duty cases. A well known
example is "it is forbidden to smoke, and if you do smoke, you must smoke
politely." To express rules that take effect only once a condition holds, the
notation switches to a dyadic form: `O (use_ashtray | smoke)`, read as "given
that you smoke, using an ashtray is obligatory." Because the condition sits
outside the `O` operator, the logic no longer forces the unwanted jump from a
blanket prohibition on smoking to a blanket obligation to smoke politely. The
extra obligation applies only in the worlds where smoking already occurs.

## Consistency checking

As obligations, permissions, and prohibitions accumulate, a quick consistency
check matters: if both `O p` and `F p` can be derived, the system both requires
and forbids the same action, which means a rule has to change.

## Summary

Keep the vocabulary compact (`drive`, `pay_tax`), label each clause with one of
`O`, `P`, or `F`, and rely on axiom K together with the duality equivalences to
derive consequences. With these steps a rulebook can be written, tested, and
revised much like a short program is debugged. Here the bugs are conflicting
duties, and the output is a consistent, ordered set of norms.
