def calcular_serie(n):
    serie = [(i / (i + 3)) for i in range(2, n + 2)]
    ultimo_termino = serie[-1]
    sumatoria = sum(serie)
    return ultimo_termino, sumatoria


cantidad_terminos = int(input("Ingrese cuántos números desea calcular en la serie: "))

ultimo_termino, sumatoria = calcular_serie(cantidad_terminos)

print("Resultados:")
print("Ultimo término: {:.3f}".format(ultimo_termino))
print("Sumatoria: {:.3f}".format(sumatoria))
