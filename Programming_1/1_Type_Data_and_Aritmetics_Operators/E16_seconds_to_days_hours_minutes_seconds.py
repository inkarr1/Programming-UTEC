# Desarrolle un programa que permita convertir segundos a: días, horas, minutos y segundos.
# El programa deberá mostrar el equivalente de los segundos utilizando el formato:
# D:HH:MM:SS,  donde  D,HH,MM  y  SS  representan  los  días,  horas,  minutos  y  segundos
# respectivamente.
# Las horas, minutos y segundos deberá formatearse de tal manera que solo ocupe exactamente
# dos dígitos, incluyendo el 0 si es necesario.

seconds = int(input("Segundos: "))

seconds_day = 86400
seconds_hour = 3600
seconds_minute = 60

dd = seconds // seconds_day
seconds = seconds % seconds_day
hh = seconds // seconds_hour
seconds = seconds % seconds_hour
mm = seconds // seconds_minute
ss = seconds % seconds_minute

print("Equivale a: %d:%02d:%02d:%02d" % (dd, hh, mm, ss))