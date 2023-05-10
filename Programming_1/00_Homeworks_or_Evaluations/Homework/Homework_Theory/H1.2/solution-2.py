# NO MODIFICAR NADA BAJO ESTA LINEA
def main():
    # NO MODIFICAR NADA SOBRE ESTA LINEA

    # ============Pregunta 1=================
    promedio = float(input("promedio: "))
    apellido = str(input("apellido: "))
    # Codigo para Pregunta 1 comienza aqui

    if promedio >= 17.5:
        seccion = "A"
    elif 14 <= promedio < 17.5:
        seccion = "B"
    elif 11 <= promedio < 14:
        seccion = "C"
    else:
        seccion = "D"

    if apellido[0].upper() < "N":
        grupo = "1"
    else:
        grupo = "2"

    print(f"{seccion}{grupo}")
    # Codigo par Pregunta 1 termina aquí. Recuerda imprimir el resultado final. NO DEJES EL PRINT VACÍO.

    # ============Pregunta 2=================
    votaciones = str(input("votación: "))
    # Codigo para Pregunta 2 comienza aqui
    candidato_a = 0
    candidato_b = 0
    candidato_x = 0

    for voto in votaciones:
        if voto == "a":
            candidato_a += 1
        elif voto == "b":
            candidato_b += 1
        else:
            candidato_x += 1

    votaciones_total = candidato_a + candidato_b
    percent_a = (candidato_a / votaciones_total) * 100
    percent_b = (candidato_b / votaciones_total) * 100
    if percent_a > 40 or percent_b > 40:
        if percent_a > percent_b:
            print("winner: a")
        elif percent_b > percent_a:
            print("winner: b")
        else:
            print("no winner")
    else:
        print("no winner")
    # Codigo par Pregunta 2 termina aquí. Recuerda imprimir el resultado final. NO DEJES EL PRINT VACÍO.
    
    # ============Pregunta 3=================
    N = int(input("N: "))
    # Codigo para Pregunta 3 comienza aqui
    i = 0
    cant_hit = 0

    while i < N:
        album_name = str(input("nombre: "))
        language = str(input("idioma: "))
        reproductions = int(input("reproducciones: "))

        if language == "español":
            if reproductions >= 1000000:
                cant_hit += 1

        i += 1

    if cant_hit >= 3:
        print("grammy latino")
    else:
        print("sin premio")
    # Codigo par Pregunta 3 termina aquí. Recuerda imprimir el resultado final. NO DEJES EL PRINT VACÍO.

# NO MODIFICAR NADA BAJO ESTA LINEA
if __name__ == '__main__':
    main()
# NO MODIFICAR NADA SOBRE ESTA LINEA