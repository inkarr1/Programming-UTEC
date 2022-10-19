number_days = int(input("Ingrese cantidad de dias: "))

sum_tasks = 0
i = 0

while i < number_days:
    print("Ingrese las tareas para el dia", i + 1)
    while True:
        number_task = float(input("Duracion de tarea en horas [0 para terminar]: "))

        sum_tasks = sum_tasks + number_task

        if number_task == 0:
            break

    i += 1

convert = sum_tasks
hour = convert // 1
minutes = (convert % 1) * 60


print("La suma de horas es:", sum_tasks)
print("Las tareas tomaron:", "{:.0f}".format(hour), "horas", "{:.0f}".format(minutes), "minutos")