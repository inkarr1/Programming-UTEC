seconds_input = int(input("Ingrese la cantidad de segundos que deseas calcular: "))

minutes = seconds_input // 60
seconds_output = seconds_input % 60

print(f"{seconds_input} segundos son {minutes} minutos {seconds_output} segundos")