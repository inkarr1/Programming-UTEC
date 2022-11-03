import random

num_input = int(input("Ingrese el tamaño: "))

lista = [ ]

for i in range(num_input):
    lista_ran = random.randrange(1000, 9999)
    lista.append(lista_ran)
print(str(lista)[1:-1])

maxRepeticiones = 0
maxNumero = -1
list_digits = [0, 4, 4, 5]

for elem in list_digits:
    repeticiones = list_digits.count(elem)
    if repeticiones > maxRepeticiones:
        maxRepeticiones = repeticiones
        maxNumero = elem

print(f"Digito {str(maxNumero)}: {str(maxRepeticiones)} repeticiones")

print("Los menores digitos son: ")

