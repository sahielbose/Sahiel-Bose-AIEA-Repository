% family.pl - Knowledge Base

% Facts
parent(john, mary).
parent(john, mike).
parent(susan, mary).
parent(susan, mike).
parent(mike, anna).
parent(mike, james).
parent(linda, anna).
parent(linda, james).
male(john).
male(mike).
male(james).
female(susan).
female(mary).
female(linda).
female(anna).

% Rule: A grandparent relationship
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
