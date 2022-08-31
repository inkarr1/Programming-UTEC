# Realice un programa que permita leer un número entero de 3 dígitos
# y el programa imprima el número al revés.
# Desarrolle el programa utilizando los operadores matemáticos y trabaje
# bajo el supuesto que el usuario siempre ingresará un número de 3 dígitos

num = int(input("Numero: "))

while num >= 1:
    num_rpta = num%10
    num = num//10
    result = num_rpta

print("Numero invertido: ", result)