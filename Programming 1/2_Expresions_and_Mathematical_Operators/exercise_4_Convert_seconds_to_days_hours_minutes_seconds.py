# Desarrolle un programa que permita convertir  segundos a: dias, horas, minutos y segundos.
# El programa deberá mostrar el equivalente de los segundos utilizando el formato:
# D:HH:MM:SS, donde D,HH,MM y SS representan los días, horas, minutos y segundos respectivamente.
# Las horas, minutos y segundos deberá formatearse de tal manera que solo ocupe exactamente dos digitos,
# incluyendo el 0 si es necesario.

num = int(input("Ingrese los segundos: "))

days = num//(24*60*60)
num = num%(24*60*60)

hours = num//(60*60)
num = num%(60*60)

minutes = num//(60)
seconds = num%(60)

print("Equivale a: ", days, ":", hours, ":", minutes, ":", seconds)