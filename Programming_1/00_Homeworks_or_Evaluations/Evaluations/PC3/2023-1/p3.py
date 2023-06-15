n_terminos = int(input("Ingrese cuántos números desea calcular en la serie: "))

serie = [(i * ((i + 1) / (i + 2))) for i in range(1, n_terminos + 1)]
ultimo_termino = serie[-1]
sumatoria = sum(serie)

print("Resultados:")
print("Ultimo término: {:.3f}".format(ultimo_termino))
print("Sumatoria: {:.3f}".format(sumatoria))
