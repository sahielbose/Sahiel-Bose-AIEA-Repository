#check if x is a variable
def is_var(x):
    return isinstance(x, str) and x.startswith('?')

def substitute(exp, subs):
    if isinstance(exp, tuple):
        return tuple(substitute(e, subs) for e in exp)
    elif is_var(exp) and exp in subs:
        return substitute(subs[exp], subs)
    else:
        return exp
    
#find when x and y are equal and subsituting until they are with different rules
def unify(x, y, subs):
    subs = subs.copy()
    x = substitute(x, subs)
    y = substitute(y, subs)
    if x == y:
        return subs
    if is_var(x):
        subs[x] = y
        return subs
    if is_var(y):
        subs[y] = x
        return subs
    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for a, b in zip(x, y):
            subs = unify(a, b, subs)
            if subs is None:
                return None
        return subs
    return None

#check if goal matches
def bc(kb, goals, subs):
    if not goals:
        yield subs
    else:
        first, rest = goals[0], goals[1:]
        for (head, body) in kb:
            newsubs = unify(first, head, subs)
            if newsubs is not None:
                yield from bc(kb, list(body) + rest, newsubs)
                
#function for input
def ask(kb, query):
    return list(bc(kb, [query], {}))


#input to check for code
if __name__ == '__main__':
    kb = [
        (("Parent", "John", "Mary"), []),
        (("Parent", "Mary", "Susan"), []),
        (("Grandparent", "?x", "?y"), [(("Parent", "?x", "?z")), (("Parent", "?z", "?y"))])
    ]
    query = ("Grandparent", "John", "?who")
    answers = ask(kb, query)
    print("Answers:", answers)