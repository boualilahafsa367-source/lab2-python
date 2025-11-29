#Exercice 2: Conversion de températures

X=float(input("Entrer une valeur : "))
print("Choisissez le sens de conversion : ")
print("1.en Fahrenheit et Kelvin  ")
print("2.en Celsius et kelvin ")
print("3.en Celsius et Fahrenheit ")
choix=int(input("Votre choix est : "))
if choix==1:
    F = X * 9 / 5 + 32
    K = X + 273.15
    print(f"{X}°C = {F}°F = {K}K")
elif choix == 2:
    C = (X - 32) * 5/9
    K= C + 273.15
    print(f"{X}°F = {C}°C = {K}K")
elif choix == 3:
    C = X-273.15
    F= C * 9/5 + 32
    print(f"{X}K = {C}°C = {F}°F")
else :
    print("Choix invalide!")
