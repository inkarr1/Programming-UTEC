lista = [
{'ciudad':'La Rinconada', 'altitud': 5100, 'departamento':'Puno', 'poblacion': 17000},
{'ciudad':'Cerro de Pasco', 'altitud': 4380, 'departamento':'Pasco', 'poblacion': 66860},
{'ciudad':'Junin', 'altitud': 4105, 'departamento':'Junin', 'poblacion': 10000},
{'ciudad':'Yauri', 'altitud': 3976, 'departamento':'Cusco', 'poblacion': 29772},
{'ciudad':'Yanaoca', 'altitud': 3913, 'departamento':'Cusco', 'poblacion': 11000},
{'ciudad':'Ayaviri', 'altitud': 3907, 'departamento':'Puno', 'poblacion': 20152},
{'ciudad':'Lampa', 'altitud': 3878, 'departamento':'Puno', 'poblacion': 14780},
{'ciudad':'Ilave', 'altitud': 3862, 'departamento':'Puno', 'poblacion': 22153},
{'ciudad':'Azangaro', 'altitud': 3859, 'departamento':'Puno', 'poblacion': 35230},
{'ciudad':'Juli', 'altitud': 3850, 'departamento':'Puno', 'poblacion': 23741},
{'ciudad':'Yunguyo', 'altitud': 3847, 'departamento':'Puno', 'poblacion': 11890},
{'ciudad':'Juliaca', 'altitud': 3824, 'departamento':'Puno', 'poblacion': 216716},
{'ciudad':'Puno', 'altitud': 3810, 'departamento':'Puno', 'poblacion': 120229},
{'ciudad':'La Oroya', 'altitud': 3745, 'departamento':'Junín', 'poblacion': 29417},
{'ciudad':'Huancavelica', 'altitud': 3676, 'departamento':'Huancavelica', 'poblacion': 41331},
{'ciudad':'Sicuani', 'altitud': 3549, 'departamento':'Cusco', 'poblacion': 42551},
]


def citySearch(nombre_ciudad):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        ciudad = lista[medio]['ciudad']

        if ciudad == nombre_ciudad:
            return lista[medio]
        elif ciudad < nombre_ciudad:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None


ciudad1 = input("Ingrese la ciudad: ")
datos_ciudad1 = citySearch(ciudad1)

if datos_ciudad1 is None:
    print(f"No fue encontrado")
else:
    print(datos_ciudad1)
print("")
ciudad2 = input("Ingrese la ciudad: ")
datos_ciudad2 = citySearch(ciudad2)

if datos_ciudad2 is None:
    print(f"No fue encontrado")
else:
    print(datos_ciudad2)

print("")
if (datos_ciudad1 and datos_ciudad2) is True:
    diferencia_altitud = datos_ciudad1['altitud'] - datos_ciudad2['altitud']
    diferencia_poblacion = datos_ciudad1['poblacion'] - datos_ciudad2['poblacion']

    if diferencia_altitud < 0:
        ciudad_mayor_altitud = ciudad2
        diferencia_altitud = -diferencia_altitud
    else:
        ciudad_mayor_altitud = ciudad1

    if diferencia_poblacion < 0:
        ciudad_mayor_poblacion = ciudad2
        diferencia_poblacion = -diferencia_poblacion
    else:
        ciudad_mayor_poblacion = ciudad1

    print(f"Diferencia de altitud: {diferencia_altitud}")
    print(f"Diferencia de poblacion: {diferencia_poblacion}")
else:
    print("No se puede hallar la diferencia")

