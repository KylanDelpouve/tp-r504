import fonctions as f

#===============================
# Q2.3
# boucle infinie
while True:
   a = int(input("Entrez la nombre a : "))
   b = int(input("Entrez le nombre b : "))
   res = f.puissance(a, b) # appel de la fonction puissance et stockage du résultat
   print(f"{a} élevé à la puissance {b} est égale à : {res}")
#===============================

#===============================
# Q2.5
#print("Test avec un flottant :")
#res = f.puissance (2.5, 3)
#print(f"Résultat : {res}")
#===============================
