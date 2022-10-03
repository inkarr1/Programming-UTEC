# Diseñe un algoritmo e implemente un programa que permita jugar: "Adivina el número". El programa
# seleccionará un número aleatorio entre 1 y 10 preguntará al usuario que ingrese un número hasta
# que lo adivine.

import random

number = random.randint(1, 10)
intent = 0

while intent != number:
    intent = int(input("Intente adivinar el número: "))

    if intent == number:
        print("Felicitaciones adivinó el número!!!")
    else:
        print("No adivinó. Siga intentando.")