print("DATOS:")
sex = input("1. REGISTRAR SEXO (Hombre: H / Mujer: M): ").upper()
height = float(input("2. REGISTRAR ALTURA (Mts.): "))
weight = int(input("3. REGISTRAR PESO (Kg.): "))
age = int(input("4. REGISTRAR EDAD (Años): "))

mme_result = (-0.00137 * (age ** 2)) + (0.1074 * (height * 100)) + ((0.3362 * weight + 6.93) * (sex == "H")) + ((0.2462 * weight + 12.04) * (sex == "M"))

print("EL CALCULO DE LA MASA MUSCULAR ESQUELETICA:")
print("{:.3f}".format(mme_result), "Kg.")
