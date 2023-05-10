n_mediciones = int(input("Numero de mediciones de calidad de aire: "))
i = 0
n_bueno = 0
n_moderado = 0
n_danino = 0
n_muydanino = 0

while n_mediciones < 5 or n_mediciones > 40:
    n_mediciones = int(input("Numero de mediciones de calidad de aire: "))

while i < n_mediciones:
    cantidad_medicion = int(input("Ingrese la medicion: "))
    if cantidad_medicion <= 50:
        n_bueno += 1
    elif cantidad_medicion <= 100:
        n_moderado += 1
    elif cantidad_medicion <= 150:
        n_danino += 1
    else:
        n_muydanino += 1
    i = i + 1
print("Nivel bueno:", "{:.3f}".format((n_bueno * 100) / n_mediciones))
print("Nivel moderado:", "{:.3f}".format((n_moderado * 100) / n_mediciones))
print("Nivel dañino:", "{:.3f}".format((n_danino * 100) / n_mediciones))
print("Nivel muy dañino:", "{:.3f}".format((n_muydanino * 100) / n_mediciones))
