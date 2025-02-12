print("formulaire d'emploi")# voici le formulaire d'emploi pour un poste de développeur web

experience = input("aviez-vous de l'expérience dans le domaine? ")# question 1 qui se repondera par oui ou non

if experience == "oui":
    print("parfait, prochaine question")

elif experience == "non":
    print("ok, question suivante")

else :
    print("mauvaise entrée")
while True:
    experience = input("aviez-vous de l'expérience dans le domaine? ")
    if experience == "non" or experience == "oui":
        break
    else:
        print("mauvaise entrée")# si ce nest pas oui ou non, on vous redemande de repondre oui ou non
            
    

for année_exp in range(100):#pour cette question, on vous demande de rentrer un chiffre entre 0 et 100
    print(f"{année_exp} ans d'expérience")

while True:
    année_exp = input("combien d'années d'expérience? ")#si ce nest pas un chiffre, on vous redemande de rentrer un chiffre

    if année_exp.isdigit():  # répondre en chiffres svp
        année_exp = int(année_exp)

        if année_exp < 5:
            print("pas assez d'expérience.")# si vous avez moins de 5 ans d'expérience, vous n'êtes pas accepté
            break

        elif année_exp >= 5:
            print("parfait, prochaine question")#si vous avez 5 ans ou plus d'expérience, vous passez à la prochaine question
            break

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
    while True:
        diplôme = input("avez-vous un diplôme en lien avec ce domaine? ")
        if diplôme == "non" or diplôme == "oui":
            break
        else:
            print("mauvaise entrée")

if experience == "oui" and année_exp >= 5 and diplôme == "oui":
    print("félicitations, vous avez le travail!")

else:
    print("on vous rappele.")


print("ce n'est pas fini si vous n'aviez pas été accepté")
question = input ("aviez-vous répondu non a l'une des questions?")

while True:
    question = input("aviez-vous répondu non à l'une des questions? ")
    if question == "non":
        print("vous aviez terminé le formulaire veuillez le deposer")
        break
    elif question == "oui":
        print("ce n'est pas fini")
        break
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