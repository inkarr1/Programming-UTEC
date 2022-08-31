# Escriba  un programa que reciba un número representado una cantidad de
# segundos. Posteriormente, el programa deberá calcular cuantos minutos
# y segundos hay ese tiempo. Por ejemplo: 150 segundos -> 2 minutos 30 segundos

seconds_input = int(input("Ingrese la cantidad de segundos que deseas calcular: "))

minutes = seconds_input // 60
seconds_output = seconds_input % 60

print(f"{seconds_input} segundos son {minutes} minutos {seconds_output} segundos")