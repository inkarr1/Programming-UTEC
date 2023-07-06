calidad_aire = [
    {'pais':'Bhutan', 'aire': 28.71, 'expectativa': -2.32},
    {'pais':'India', 'aire': 55.80, 'expectativa': -4.98},
    {'pais':'Nepal', 'aire': 47.13, 'expectativa': -4.13},
    {'pais':'Pakistan', 'aire': 44.17, 'expectativa': -3.84},
    {'pais':'Rwanda', 'aire': 32.95, 'expectativa': -2.74},
    {'pais':'Burundi', 'aire': 31.76, 'expectativa': -2.62},
    {'pais':'China', 'aire': 31.63, 'expectativa': -2.61},
    {'pais':'Equatorial Guinea', 'aire': 28.61, 'expectativa': -2.31},
    {'pais':'Guatemala', 'aire': 28.45, 'expectativa': -2.30},
    {'pais':'Bangladesh', 'aire': 75.76, 'expectativa': -6.93},
    {'pais':'Cameroon', 'aire': 31.42, 'expectativa': -2.59},
    {'pais':'Qatar', 'aire': 29.19, 'expectativa': -2.37},
    {'pais':'Mongolia', 'aire': 31.47, 'expectativa': -2.59},
    {'pais':'Laos', 'aire': 28.00, 'expectativa': -2.25},
]

campo = input("Ingrese campo para ordenar (pais, expectativa): ")

if campo == "pais":
    calidad_aire.sort(key=lambda x: x['pais'], reverse=True)
elif campo == "expectativa":
    calidad_aire.sort(key=lambda x: x['expectativa'])
else:
    print("Campo no válido.")

print("La lista ordenada por", campo, "es:")

for item in calidad_aire:
    print(f"{item['pais']:20s}{item['aire']:5.2f} {item['expectativa']:5.2f}")
