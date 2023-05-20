phrase = "Estamos desarrollando un código en Python"
letter = "s"
contador = 0

for i in phrase:
    if i == letter:
        contador += 1
print("la letra", letter, "aparece", contador,"veces en la frase", phrase)
