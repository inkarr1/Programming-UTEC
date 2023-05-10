number = int(input("Ingrese un número: "))

suma = number
i = 0

while number != 0:
    number = int(input("Ingrese un número: "))
    suma += number
    print("suma:",suma)
    if number == 0:
        suma += number
    i += 1
print(f"{suma}/ {i} =",suma/i)