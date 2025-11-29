#Exercice 3: Analyse de texte utilisateur
Texte =input("veuillez saisir  un mot ou une phrase : ")
Longueur=len(Texte)
Majuscule=str.upper(Texte)
Minuscule=str.lower(Texte)
inversion=Texte[::-1]
#ici la chaine originale donnee par l'utilisateur a ete modifiee (modification de la variable sur place), on a cree une nouvelle chaine)
print("la longueur du mot / phrase sasie est:" ,Longueur)
print("mot / phrase sasie en majuscule :",Majuscule)
print("mot / phrase sasie en minuscule :",Minuscule)
print("mot / phrase sasie en inversion :",inversion)
# conservation de la chaine originale !
Texte =input("veuillez saisir  un mot ou une phrase : ")
Texte1=Texte
Longueur=len(Texte1)
Majuscule=str.upper(Texte1)
if Majuscule==Texte :
    print ("les deux chaines sont identiques")
else:
    print ("les deux chaines sont differents")
Minuscule=str.lower(Texte1)
inversion=Texte1[::-1]
