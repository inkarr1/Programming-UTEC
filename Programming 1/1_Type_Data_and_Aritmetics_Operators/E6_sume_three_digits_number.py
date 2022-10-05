# Desarrolle unprograma que permita hallar la suma de los digitos de un numero de 3 digitos.

numero = int(input("Numero de 3 cifras: "))

unidades = numero % 10
decenas  = numero // 10 % 10
centenas = numero // 100

suma =  unidades + decenas  + centenas

print("La suma de los digitos es: ", suma)