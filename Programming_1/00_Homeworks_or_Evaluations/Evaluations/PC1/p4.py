n_students = int(input("Cantidad de alumnos: "))
i = 0
ctg_down = 0
ctg_promedy = 0
ctg_hight = 0
ctg_superior = 0

while n_students < 5 or n_students > 50:
    n_students = int(input("Cantidad de alumnos: "))

while i < n_students:
    reading_velocity = int(input("Ingrese la cantidad de palabras por minuto: "))
    if reading_velocity <= 139:
        ctg_down += 1
    elif reading_velocity <= 186:
        ctg_promedy += 1
    elif reading_velocity <= 234:
        ctg_hight += 1
    else:
        ctg_superior += 1
    i = i + 1
print("Bajo:", "{:.3f}".format((ctg_down * 100) / n_students))
print("Promedio:", "{:.3f}".format((ctg_promedy * 100) / n_students))
print("Alto:", "{:.3f}".format((ctg_hight * 100) / n_students))
print("Superior:", "{:.3f}".format((ctg_superior * 100) / n_students))