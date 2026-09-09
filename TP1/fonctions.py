def puissance(a, b):
    if not type(a) is int or not type(b) is int: # vérifie si a et b sont des entiers
        raise TypeError("Only integers are allowed") # si a ou b n'est pas un entier, lance une erreur
    return a ** b