#le "def resultat" sert à regrouper le calcul qui sera renvoyé dans le main.py
def resultat(op, nbr1, nbr2):
    if op == "A":
        print(nbr1, "+", nbr2, "=", nbr1 + nbr2)
    elif op == "S":
        print(nbr1, "-", nbr2, "=", nbr1 - nbr2)
    elif op == "M":
        print(nbr1, "*", nbr2, "=", nbr1 * nbr2)
    elif op == "D":
        #vérification que le dénominateur n'est pas 0
        if nbr2 != 0:
            print(nbr1, "/", nbr2, "=", nbr1 / nbr2)
        else:
            print("Il est impossible de diviser par zéro")
