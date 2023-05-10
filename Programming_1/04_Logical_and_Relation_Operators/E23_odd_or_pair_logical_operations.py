number = int(input("Number: "))

# numero = int(input("Ingrese un numero entero: ")
# par = (numero%2==0)
# impar = (numero%2!==0)
# print("El numero es: " + ((par)*"par") + ((impar)*"impar")

result = "Es" + " " + ("im" * (number % 2 == 1)) + "par"

print(result)