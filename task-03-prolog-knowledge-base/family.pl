% family.pl - Family relations knowledge base
%
% Facts describe direct parent relationships and the sex of each individual.
% The grandparent rule is derived through resolution over the parent facts.

% Facts: parent(Parent, Child)
parent(john, mary).
parent(john, mike).
parent(susan, mary).
parent(susan, mike).
parent(mike, anna).
parent(mike, james).
parent(linda, anna).
parent(linda, james).

% Facts: sex of each individual
male(john).
male(mike).
male(james).
female(susan).
female(mary).
female(linda).
female(anna).

% Rule: X is a grandparent of Y when X is a parent of some Z
% who is in turn a parent of Y.
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
