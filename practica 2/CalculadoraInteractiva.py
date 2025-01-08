# Primer número (pot ser enter o decimal)
# Demanem a l'usuari que introdueixi el primer número i el convertim a tipus float per permetre valors decimals.
primer_numero = float(input("Introdueix el primer número: "))

# Segon número (pot ser enter o decimal)
# Demanem a l'usuari que introdueixi el segon número i el convertim a tipus float per permetre valors decimals.
segon_numero = float(input("Introdueix el segon número: "))

# Operació a realitzar (+, -, *, /, %)
# Demanem a l'usuari que introdueixi l'operació matemàtica que vol realitzar entre els dos números.
operacio = input("Introdueix l'operació (+, -, *, /, %): ")

# Operació:
# Comprovem quina operació s'ha seleccionat i realitzem el càlcul corresponent.
if operacio == "+":
    # Suma dels dos números
    resultat = primer_numero + segon_numero
    # Mostrem el resultat de la suma
    print("Resultat de", primer_numero, "+", segon_numero, "=", resultat)  # En un print, les variables es posen sense cometes i el text amb cometes

elif operacio == "-":
    # Resta dels dos números
    resultat = primer_numero - segon_numero
    # Mostrem el resultat de la resta
    print("Resultat de", primer_numero, "-", segon_numero, "=", resultat) 

elif operacio == "*":
    # Multiplicació dels dos números
    resultat = primer_numero * segon_numero
    # Mostrem el resultat de la multiplicació
    print("Resultat de", primer_numero, "*", segon_numero, "=", resultat)

elif operacio == "/":
    # Divisió dels dos números, sempre que el divisor no sigui zero
    if segon_numero != 0:
        resultat = primer_numero / segon_numero
        # Mostrem el resultat de la divisió
        print("Resultat de", primer_numero, "/", segon_numero, "=", resultat)
    else:
        # Missatge d'error si es divideix per zero
        print("La divisió no és correcta!")

elif operacio == "%":
    # Càlcul del mòdul entre els dos números, sempre que el divisor no sigui zero
    if segon_numero != 0:
        resultat = primer_numero % segon_numero
        # Mostrem el resultat del mòdul
        print("Resultat de", primer_numero, "%", segon_numero, "=", resultat)
    else:
        # Missatge d'error si es calcula el mòdul amb divisor zero
        print("No es pot calcular!")

else:
    # Missatge d'error si l'operació introduïda no és vàlida
    print("Operació invàlida! Introdueix l'operació correctament (+, -, *, /, %).")

