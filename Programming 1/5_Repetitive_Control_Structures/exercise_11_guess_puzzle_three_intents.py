# JUEGO ADIVINA EL NÚMERO
# Modifique el programa del juego, con la finalidad que cuando imprima el mensaje
# "No adivinó. Siga intentando", adicionalmente, también imprima una ayuda señalando:
# "El número a adivinar es menor" o "El número a adivinar es mayor"

import random

number = random.randint(1,10)
intent = 0
i = 1

while intent != number:
    intent = int(input("Intente adivinar el número: "))

    if intent == number:
        print("Felicitaciones adivinó el número!!!")
    else:
        print("No adivinó. Siga intentando.")
        if (intent > number):
            print("El número a adivinar es menor.")
        else:
            print("El número a adivinar es mayor.")
    if i == 3: break
    i += 1