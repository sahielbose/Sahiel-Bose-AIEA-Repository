"""Resolve a conjunctive query over the family knowledge base.

The query parent(john, X), parent(X, anna) asks for every X that is both a
child of john and a parent of anna, exercising Prolog's ability to chain
multiple goals and bind shared variables across them.
"""

from pyswip import Prolog

# Initialize Prolog
prolog = Prolog()

# Load the Prolog file
prolog.consult("family.pl")

# Query: Find X such that John is X's parent and X is Anna's parent
query = list(prolog.query("parent(john, X), parent(X, anna)"))

# Print results
if query:
    for result in query:
        print(f"X = {result['X']}")
else:
    print("No results found.")