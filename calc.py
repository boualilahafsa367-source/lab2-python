# Exercice 1 : Mini-Calculatrice
nombre_1= float(input("veuillez entrer le premier nombre: "))
nombre_2 = float(input("veuillez entrer le deuxieme nombre: "))
print("Choisissez une opération :")
print("1_ Addition")
print("2_ Soustraction")
print("3_ Multiplication")
print("4_ Division réelle")
choix = int (input("Votre choix est : "))
if choix == 1:
    Somme=nombre_1+nombre_2
    print(f"{nombre_1} + {nombre_2} = {Somme}")
elif choix == 2:
    Resultat=nombre_1-nombre_2
    print(f"{nombre_1} - {nombre_2} = {Resultat}")
elif choix == 3:
    Produit=nombre_1*nombre_2
    print(f"{nombre_1} * {nombre_2} = {Produit}")
elif choix == 4:
    if nombre_2!=0:
        Quotient=nombre_1/nombre_2
        print(f"{nombre_1} / {nombre_2} = {Quotient}")
    else:
        print("division par 0 est impossible")
else:
    print("choix est invalide ! ")



