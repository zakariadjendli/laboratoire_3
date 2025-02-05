print("formulaire d'emploi")

experience = input("aviez-vous de l'expérience dans le domaine? ")

if experience == "oui":
    print("parfait, prochaine question")

elif experience == "non":
    print("ok, question suivante")

else:
    print("mauvaise entrée")

année_exp = input("combien d'années d'expérience? ")

if année_exp.isdigit(): # repondre en chiffres svp
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
    print("on vous rappele.")


print("ce n'est pas fini si vous n'aviez pas été accepté")
question = input ("aviez-vous répondu non a l'une des questions?")

if question == "non":
    print("vous aviez terminé le formulaire veuillez le deposer")
elif question == "oui":
    print("ce n'est pas fini")
else:
    print("mauvaise entrée")


print("besoin d'infos pour les stats")
exp = input ("je vois que vous n'aviez pas assez d'experience, expliquez-moi pourquoi?")   # pas de bonnes ou mauvaises réponses
print("ok je vois")



print("une derniere question?")
qqq= input ("le diplome est-il pour bientot?")
if qqq == "oui":
    print("n'hesitez pas a revenir postuler")

elif qqq == "non":
    print ("je vous souhaite bonne chance pour les autres entretiens")


    

# If et elif soi oui et non 
# else tout le reste sera pas enregistré et vous dira mauvaise entrée

            #3 bloc de conditions complet,3 entrées utilisateur,1 operateur logique,imprimer un resultat # op log 