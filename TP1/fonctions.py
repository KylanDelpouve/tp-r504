def puissance(a, b):
    if not type(a) is int or not type(b) is int: # verifie si a et b sont des entiers
        raise TypeError("Only integers are allowed") # si a ou b n'est pas un entier, lance une erreur

    if a == 0 and b < 0:
        raise ZeroDivisionError("0 ne peut pas etre eleve a une puissance negative")

# tout nombre eleve puissance 0 donne 1
    if b == 0:
        return 1

    res = 1 # initialisation du resultat a 1 pour preparer les muliplications
    exp = abs(b) # on prend valeur absolue de b pour que la boucle tourne un nombre positif de fois
    # on repete la multiplication en fonction de l'exposant
    for _ in range(exp):
        res = res * a # a chaque boucle, on multiplie le resultat precedent par a
    if b < 0:
        return 1 / res

    return res

#    return a ** b
