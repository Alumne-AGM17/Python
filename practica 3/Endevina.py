import random

def joc_endevina_numero():
    # Procedim a generar un numero aleatori entre l'1 i el 100
    numero_pensat = random.randint(1, 100)
    
    # Definim els limits d'intents
    intents_maxims = 5
    intents = 0

    # Informem a l'usuari sobre el nombre de intents i l'objectiu del joc
    print("He memoritzat un numero de l'1 al 100. Tens 5 intents per endevinar-lo.")

    # Bucle per controlar el nombre d'intents
    while intents < intents_maxims:
        # Incrementem el comptador d'intents
        intents += 1

        # L'usuari ha d'introduir un numero
        print("Intent", intents, "- Quin numero he pensat?: ")
        resposta_usuari = int(input())

        # Comprovem si el numero introduit per l'usuari es igual al numero pensat
        if resposta_usuari == numero_pensat:
            # Si encerta, mostrem un missatge de felicitacio i sortim del bucle
            print("Enhorabona! Has encertat en", intents, "intents!")
            break
        elif resposta_usuari < numero_pensat:
            # Si el numero es mes petit, informem a l'usuari que el numero pensat es mes gran
            print("El numero es mes gran.")
        else:
            # Si el numero es mes gran, informem a l'usuari que el numero pensat es mes petit
            print("El numero es mes petit.")

        # Comprovem si s'ha superat el nombre maxim d'intents
        if intents == intents_maxims:
            # Si l'usuari ha esgotat els intents, informem del numero correcte
            print("Ho sento, has esgotat els teus", intents_maxims, "intents. El numero era", numero_pensat, ".")

# Executar el joc
joc_endevina_numero()
