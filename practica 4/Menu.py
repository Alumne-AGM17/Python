# Llistes
# Inicialitzem dues llistes buides: una per als plats i una altra per als preus corresponents.
plats = []
preus = []

# Comanda dels plats i els seus preus corresponents
# Demanem a l'usuari que introdueixi fins a un maxim de 8 plats amb els seus preus (L'usuari pot parar la comanda escrivint "$" o amb un preu de valor zero o negatiu)
while len(plats) < 8:
    plat = input("Afegeix un plat $ per acabar: ")
    if plat == "$":
        # Si l'usuari introdueix "$", sortim del bucle.
        break
    preu = float(input("Introdueix el preu de {}: ".format(plat)))
    if preu <= 0:
        # Si el preu és zero o negatiu, sortim del bucle.
        break
    # Afegim el plat i el seu preu a les llistes corresponents.
    plats.append(plat)
    preus.append(preu)

# Opció "PAGAR" a les llistes
# Afegim l'opció "PAGAR" al final de la llista de plats, amb un preu de 0.
plats.append("PAGAR")
preus.append(0)

# Mostrar el menú
# Mostrem el menu amb els plats i els preus.
print("MENU")
print("----------")
for i in range(len(plats)):
    # Mostrem cada plat amb el seu numero i el preu corresponent.
    print(f"{i+1} - {plats[i]} ... {preus[i]}€")
print("----------")

# Cost total
# Inicialitzem una variable per guardar el cost total dels plats seleccionats.
cost_total = 0

# L'usuari selecciona un plat fins que decideixi "PAGAR"
# Demanem a l'usuari que esculli un plat fins que decideixi pagar escrivint "0"
while True:
    eleccio = input("Que volen dinar (Escriu 0 per pagar)? ")
    if eleccio == "0":
        # Si l'usuari escriu "0", sortim del bucle.
        break
    try:
        # Intentem convertir l'elecció a un numero enter.
        eleccio = int(eleccio)
        # Sumem el preu del plat seleccionat al cost total.
        cost_total += preus[eleccio - 1]
        # Mostrem el plat seleccionat i el seu preu.
        print(f"Heu seleccionat {plats[eleccio - 1]} per {preus[eleccio - 1]}€")

    except (ValueError, IndexError):
        # Si hi ha un error amb la conversió o l'index és incorrecte, mostrem un missatge d'error.
        print("Error: elecció incorrecta")

# Mostrar el cost total
# Un cop l'usuari ha decidit pagar, mostrem l'import total.
print(f"L'import total és de: {cost_total}€")
