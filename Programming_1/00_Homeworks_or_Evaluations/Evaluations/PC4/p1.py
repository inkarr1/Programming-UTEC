def sumatoriaTerminos(number):
    serie = [(i * ((i + 1) / (i + 2))) for i in range(1, number + 1)]
    return serie


def isRecursiveSerie(number):
    sumatoria = sum(sumatoriaTerminos(number))
    result = "{:.3f}".format(sumatoria)
    return result


cant_terminos = int(input("Cantidad de terminos: "))
print("Resultado:")
print(isRecursiveSerie(cant_terminos))
