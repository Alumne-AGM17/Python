# Dades de l'Usuari
# Sol·licitem a l'usuari que introdueixi el seu DNI, el preu de l'article, el percentatge de descompte i el percentatge d'IVA.
DNI = input("Afegeix el DNI del client: ")
preu_article = float(input("Afegeix el preu de l'article: "))
descompte = float(input("Afegeix el percentatge del descompte: "))
iva = float(input("Afegeix el percentatge d'IVA: "))

# Càlcul de descompte
# Calculem el descompte en funció del percentatge donat i restem aquest valor al preu de l'article.
descompte = (descompte / 100) * preu_article
preu_amb_descompte = preu_article - descompte

# Càlcul del NIF
# Calculem la lletra corresponent al DNI utilitzant l'algorisme de mòdul 23, i la concatenem amb el número de DNI.
lletraDNI = "TRWAGMYFPDXBNJZSQVHLCKE"
print(DNI + lletraDNI[int(DNI) % 23])  # Mostrem el DNI amb la lletra corresponent
NIF = DNI + lletraDNI[int(DNI) % 23]   # Guardem el NIF complet

# Càlcul amb IVA
# Calculem l'import de l'IVA sobre el preu amb el descompte aplicat i sumem l'IVA per obtenir el preu final.
iva = (iva / 100) * preu_amb_descompte
preu_final = preu_amb_descompte + iva

# Resultats
# Mostrem tots els resultats: el DNI del client, el preu de l'article, el descompte aplicat, el preu amb descompte, l'IVA i el preu final a pagar.
print("DNI del client:", DNI)
print("Preu de l'article:", preu_article, "€")
print("Descompte aplicat:", descompte, "€")
print("Preu amb descompte:", preu_amb_descompte, "€")
print("IVA:", iva, "€")
print("Preu final a pagar:", preu_final, "€")