#Etape 1 :
entier = 42              # int
flottant = 3.14          # float
texte = "Python"         # str
vrai_ou_faux = True      # bool

#Etape 2:
print(entier, "→", type(entier))
print(flottant, "→", type(flottant))
print(texte, "→", type(texte))
print(vrai_ou_faux, "→", type(vrai_ou_faux))

#Etape 3:
age_str = input("Quel âge as-tu ? ")
print("Tu as saisi :", age_str, "→", type(age_str))

age = int(age_str)
print("Après conversion :", age, "→", type(age))

try:
    age = int(input("Quel âge as-tu ? "))
    print(f"Dans 5 ans tu auras {age + 5} ans.")
except ValueError:
    print("Saisie invalide, merci d'entrer un entier.")

#Etape 4:
nombre = 10      # nombre référence un int
print(nombre)
nombre = 10 + 5  # le même nom nombre pointe désormais vers un autre int (15)
print(nombre)

liste = [1, 2, 3]
liste.append(4)  # la référence reste la même, mais l'objet est modifié1
print(liste)

print(float("7.5"))
print(type(float("7.5")))
print(bool("False"))
print(type(bool("False")))
print(str(1234))
print(type(str(1234)))

age: int = int(input("Age ? ")) #age est une variable (:) est une annotation


