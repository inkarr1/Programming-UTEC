refran = "La curiosidad mato al gato"

for letter in refran:
    print(letter)

print("-" * 15)

for letter in range(len(refran) - 1, -1, -1):
    print(refran[letter])

print("-" * 15)

contador_letras = 0

for letter in refran:
    if letter != " ":
        contador_letras += 1
print(f"Total de letras: {contador_letras}")
