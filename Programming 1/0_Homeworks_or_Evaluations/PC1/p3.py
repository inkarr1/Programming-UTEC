numero_tareas = int(input("Ingrese la cantidad de tareas: "))
contador = 0
suma_hora = 0
suma_minuto = 0

while contador < numero_tareas:
    print("Ingrese las horas para la tarea", contador + 1)
    hora_inicio = int(input("Hora de inicio: "))
    minuto_inicio = int(input("Minutos de inicio: "))
    hora_fin = int(input("Hora de fin: "))
    minuto_fin = int(input("Minuto de fin: "))

    total_hora = hora_fin - hora_inicio
    total_minuto = minuto_fin - minuto_inicio

    suma_hora = suma_hora + total_hora
    suma_minuto = suma_minuto + total_minuto

    contador = contador + 1

print("La cantidad de horas es", suma_hora, ", y minutos es", suma_minuto)
print("Las tareas tomaron:", suma_hora + (suma_minuto//60), "horas", suma_minuto%60, "minutos")