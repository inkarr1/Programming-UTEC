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