numero = int(input("Numero de 3 cifras: "))

unidades = numero % 10
decenas  = numero // 10 % 10
centenas = numero // 100

suma =  unidades + decenas  + centenas

print("La suma de los digitos es: ", suma)