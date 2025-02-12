def mauvaise_entree():
    print("mauvaise entrée")

def poser_question(question):
    return input(question)

def main():
    print("formulaire d'emploi")

    experience = poser_question("aviez-vous de l'expérience dans le domaine? ")

    if experience == "oui":
        print("parfait, prochaine question")
    elif experience == "non":
        print("ok, question suivante")
    else:
        mauvaise_entree()
        return

    année_exp = poser_question("combien d'années d'expérience? ")

    if année_exp.isdigit():
        année_exp = int(année_exp)
        if année_exp < 5:
            print("pas assez d'expérience.")
        else:
            print("parfait, prochaine question")
    else:
        print("mauvaise entrée, veuillez entrer un nombre.")
        return

    diplôme = poser_question("avez-vous un diplôme en lien avec ce domaine? ")

    if diplôme == "oui":
        print("parfait, analyse de votre candidature...")
    elif diplôme == "non":
        print("désolé, vous ne remplissez pas toutes les conditions.")
    else:
        mauvaise_entree()
        return

    if experience == "oui" and année_exp >= 5 and diplôme == "oui":
        print("félicitations, vous avez le travail!")
    else:
        print("on vous rappele.")

    print("ce n'est pas fini si vous n'aviez pas été accepté")
    question = poser_question("aviez-vous répondu non a l'une des questions?")

    if question == "non":
        print("vous aviez terminé le formulaire veuillez le deposer")
    elif question == "oui":
        print("ce n'est pas fini")
    else:
        mauvaise_entree()
        return

    print("besoin d'infos pour les stats")
    exp = poser_question("je vois que vous n'aviez pas assez d'experience, expliquez-moi pourquoi?")
    print("ok je vois")

    print("une derniere question?")
    qqq = poser_question("le diplome est-il pour bientot?")
    if qqq == "oui":
        print("n'hesitez pas a revenir postuler")
    elif qqq == "non":
        print("je vous souhaite bonne chance pour les autres entretiens")
    else:
        mauvaise_entree()

if __name__ == "__main__":
    main()