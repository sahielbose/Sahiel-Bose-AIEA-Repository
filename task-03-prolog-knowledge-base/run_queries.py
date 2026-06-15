"""Load the family knowledge base and derive grandparent relationships.

This script demonstrates rule-based inference: the grandparent relation is
never stated as a fact. It is derived by SWI-Prolog from the parent facts and
the grandparent rule defined in family.pl.
"""

from pyswip import Prolog


def main():
    prolog = Prolog()
    prolog.consult("family.pl")

    print("Grandparent relationships derived from the knowledge base:")
    results = list(prolog.query("grandparent(X, Y)"))
    if results:
        for result in results:
            print(f"  {result['X']} is a grandparent of {result['Y']}")
    else:
        print("  No grandparent relationships found.")


if __name__ == "__main__":
    main()
