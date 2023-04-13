n = int(input("Ingrese cantidad de dias: "))
suma_hh = 0
suma_mm = 0
hh = 0
mm = 0
for j in range(1, n+1):
    print("Ingrese las tareas para el día ", j)
    hh_a = 1
    while hh_a != 0:
        hh_a = float(input("\tDuracion de tarea en horas [0 para terminar]: "))
        suma_hh += hh_a
print("La suma de hora es: {:.2f}.".format(suma_hh))
hh = int(suma_hh)
mm = round((suma_hh - hh) * 60)
print("Las tareas tomaron: ", hh, "horas", mm, "minutos.")