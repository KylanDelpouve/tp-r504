def puissance(a, b):
    if not type(a) is int or not type(b) is int: # vérifie si a et b sont des entiers
        raise TypeError("Only integers are allowed") # si a ou b n'est pas un entier, lance une erreur

    if a == 0 and b < 0:
        raise ZeroDivisionError("0 ne peut pas etre eleve a une puissance negative")

    return a ** b
