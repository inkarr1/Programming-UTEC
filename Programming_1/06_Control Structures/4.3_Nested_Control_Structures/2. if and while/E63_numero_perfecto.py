num = 0

while num < 1:
    num = int(input("Número mayor a 1: "))

sumDiv = 1
i = 2
while i < num:
    if num % i == 0:
        sumDiv += i
    i += 1

if sumDiv == num:
    print("El numero es Perfecto")
else:
    print("El numero no es Perfecto")