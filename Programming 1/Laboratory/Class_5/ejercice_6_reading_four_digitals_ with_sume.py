# Realice un programa que permita leer un número entero de 4 digitos y el programa imprima y
# se visualice la suma de los digitos tal y como se muestra en el ejemplo.

# Trabaje bajo el supuesto, que el usuario siempre ingresará un número entero de 4 digitos

number = int(input("Número: "))

digito = number % 10
number = number // 10
suma_str = str(digito)
suma = digito

digito = number % 10
number = number // 10
suma_str = str(digito) + "+" + suma_str
suma = suma + digito

digito = number % 10
number = number // 10
suma_str = str(digito) + "+" + suma_str
suma = suma + digito

digito = number % 10
number = number // 10
suma_str = str(digito) + "+" + suma_str
suma = suma + digito

print(suma_str + "=" + str(suma))