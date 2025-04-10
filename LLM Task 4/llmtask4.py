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