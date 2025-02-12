print("formulaire d'emploi")# voici le formulaire d'emploi pour un poste de développeur web

experience = input("aviez-vous de l'expérience dans le domaine? ")# question 1 qui se repondera par oui ou non

if experience == "oui":#si la reponse est oui a experience, le resultat sera parfait, prochaine question
    print("parfait, prochaine question")

elif experience == "non":#si la reponse est non a experience, le resultat sera ok, question suivante
    print("ok, question suivante")

else :
    print("mauvaise entrée")#si vous ne repondez pas par oui ou non, on vous redemande de repondre oui ou non
while True:
    experience = input("aviez-vous de l'expérience dans le domaine? ")
    if experience == "non" or experience == "oui":#si la reponse est autre que oui ou non, on vous redemande de repondre oui ou non, la boucle continue,pour sortir de la boucle, il faut repondre oui ou non
        break
    else:
        print("mauvaise entrée")# si ce nest pas oui ou non, on vous redemande de repondre oui ou non
            
    

for année_exp in range(100):#pour cette question, on vous demande de rentrer un chiffre entre 0 et 100
    print(f"{année_exp} ans d'expérience")#pour cette question,le systeme vous montre une liste de choix entre les chiffres 0 a 100

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
            print("mauvaise entrée")#si vous ne repondez pas par un chiffre, on vous redemande de repondre par un chiffre

    else:
        print("mauvaise entrée, veuillez entrer un nombre.")

diplôme = input("avez-vous un diplôme en lien avec ce domaine? ")#cette question demande si vous avez un diplôme en lien avec le domaine

if diplôme == "oui":#si vous repondez oui, vous passez à la prochaine question
    print("parfait, analyse de votre candidature...")

elif diplôme == "non":#si vous repondez non, vous n'êtes pas accepté
    print("désolé, vous ne remplissez pas toutes les conditions.")

else:
    print("mauvaise entrée")
    while True:
        diplôme = input("avez-vous un diplôme en lien avec ce domaine? ")#si vous ne repondez pas par oui ou non, on vous redemande de repondre oui ou non
        if diplôme == "non" or diplôme == "oui":
            break
        else:
            print("mauvaise entrée")

if experience == "oui" and année_exp >= 5 and diplôme == "oui":#si vous avez de l'expérience, 5 ans ou plus d'expérience et un diplôme en lien avec le domaine, vous avez le travail
    print("félicitations, vous avez le travail!")

else:
    print("on vous rappele.")#si vous navez pas de l'expérience, 5 ans ou plus d'expérience et un diplôme en lien avec le domaine,on vous rappele


print("ce n'est pas fini si vous n'aviez pas été accepté")#si vous n'avez pas été accepté, ce n'est pas fini,il reste des questions à répondre
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


print("besoin d'infos pour les stats")#le departement des ressources humaines a besoin d'informations pour les statistiques
exp = input ("je vois que vous n'aviez pas assez d'experience, expliquez-moi pourquoi?")   # pas de bonnes ou mauvaises réponses
print("ok je vois")



print("une derniere question?")
qqq= input ("le diplome est-il pour bientot?")#envie de savoir si vous avez l'intention de terminer votre diplôme bientôt
if qqq == "oui":
    print("n'hesitez pas a revenir postuler")#vous etes encouragé à revenir postuler si vous avez l'intention de terminer votre diplôme bientôt

elif qqq == "non":
    print ("je vous souhaite bonne chance pour les autres entretiens")#vous etes encouragé à postuler ailleurs si vous n'avez pas l'intention de terminer votre diplôme bientôt


    

# If et elif soi oui et non 
# else tout le reste sera pas enregistré et vous dira mauvaise entrée

            #3 bloc de conditions complet,3 entrées utilisateur,1 operateur logique,imprimer un resultat # op log 