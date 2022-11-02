import random

number = random.randint(1, 10)
intent = 0
i = 0

while intent != number:
    intent = int(input("Intente adivinar el número: "))

    if intent == number:
        print("Felicitaciones adivinó el número!!!")
    else:
        print("No adivinó. Siga intentando.")
    i = i + 1
    if (i == 2):
        break