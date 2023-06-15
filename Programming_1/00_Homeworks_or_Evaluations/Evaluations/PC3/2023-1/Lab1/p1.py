import random

# Solicitar el tamaño de la lista al usuario
tamano_lista = int(input("Ingrese el tamaño de la lista: "))

numeros_aleatorios = []

# Generar la lista de números aleatorios
for numeros in range(tamano_lista):
    numero = random.randint(100, 999)
    numeros_aleatorios.append(numero)

numeros_strings = []
for numero in numeros_aleatorios:
    numeros_strings.append(str(numero))

print(", ".join(numeros_strings))
print()
# Crear la lista de los penúltimos divisores
divisores_penultimos = []
for numero in numeros_aleatorios:
    divisor_penultimo = 1
    for divisor in range(2, int(numero/2) + 1):
        if numero % divisor == 0:
            divisor_penultimo = divisor
    divisores_penultimos.append(divisor_penultimo)

divisores_strings = []
for divisor in divisores_penultimos:
    divisores_strings.append(str(divisor))

# Imprimir la lista de divisores encontrados
print("El penultimo divisor es:")
print(", ".join(divisores_strings))
