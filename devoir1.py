print("formulaire d'emploi")

experience = input("aviez-vous de l'expérience dans le domaine? ")

if experience == "oui":
    print("parfait, prochaine question")

elif experience == "non":
    print("ok, bonne journée")

else:
    print("mauvaise entrée")

année_exp = input("combien d'années d'expérience? ")

if année_exp.isdigit():
    année_exp = int(année_exp)

    if année_exp < 5:
        print("pas assez d'expérience.")

    elif année_exp >= 5:
        print("parfait, prochaine question")

    else:
        print("mauvaise entrée")

else:
    print("mauvaise entrée, veuillez entrer un nombre.")

diplôme = input("avez-vous un diplôme en lien avec ce domaine? ")

if diplôme == "oui":
    print("parfait, analyse de votre candidature...")

elif diplôme == "non":
    print("désolé, vous ne remplissez pas toutes les conditions.")

else:
    print("mauvaise entrée")

if experience == "oui" and année_exp >= 5 and diplôme == "oui":
    print("félicitations, vous avez le travail!")

else:
    print("désolé, votre candidature n'est pas retenue.")


if


            #3 bloc de conditions complet,3 entrées utilisateur,1 operateur logique,imprimer un resultat # op log 