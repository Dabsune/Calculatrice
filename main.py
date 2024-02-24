from calcul import resultat

while True:
    # récupération de l'opération à faire auprès de l'utilisateur
    op = input(
        "\nA - Addition   |   S - Soustraction\nM - Multiplication   |   D - Division (nombre entiers)\nQ - "
        "Quitter\n\nChoisissez une"
        "opération : ")
    op = op.upper()

    # obtention + envoi des nombres à calculer vers calcul.py
    if op == "A" or op == "S" or op == "M" or op == "D":
        nbr1 = input("\nEntrez le premier nombre : ")
        nbr1 = int(nbr1)
        nbr2 = input("Entrez le second nombre : ")
        nbr2 = int(nbr2)
        resultat(op, nbr1, nbr2)

    # conditions en cas de résultats tiers
    elif op == "Q":
        print("Arrêt du programme.")
        break

    else:
        print("VOUS DEVEZ INSCRIRE LA LETTRE SITUÉ PRÈS DE L'OPÉRATION")
