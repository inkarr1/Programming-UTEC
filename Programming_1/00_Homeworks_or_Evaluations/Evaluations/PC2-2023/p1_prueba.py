n_days = int(input("Ingrese días para el registro: "))
max_score = 0
max_day = 0

for day in range(1, n_days + 1):
    ctg_bajo = 0
    ctg_promedio = 0
    ctg_alto = 0
    ctg_superior = 0

    print(f"Ingrese datos para el día {day}:")
    score = 1

    while score != 0:
        score = int(input("Palabras por minuto [0 para terminar]: "))
        if 1 <= score <= 139:
            ctg_bajo += 1
        elif 140 <= score <= 186:
            ctg_promedio += 1
        elif 187 <= score <= 234:
            ctg_alto += 1
        elif 234 < score:
            ctg_superior += 1

        if score > max_score:
            max_score = score
            max_day = day

    print(f"\nReporte día {n_days}:")
    print("Bajo:", ctg_bajo)
    print("Promedio:", ctg_promedio)
    print("Alto:", ctg_alto)
    print("Superior:", ctg_superior)
    print()

print(f"La mayor medición se registró el día {max_day} con un valor de {max_score}.")
