number = int(input("Ingrese un número: "))

suma = 0
i = 0

while number != -1:
    number = int(input("Ingrese un número: "))

    if number >= 0 and number <= 20:
        suma += number
        i += 1
print(suma/i)