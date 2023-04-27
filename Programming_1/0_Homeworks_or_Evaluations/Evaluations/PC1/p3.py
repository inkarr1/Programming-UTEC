lenght_serie = int(input("Ingrese cuantos numeros desea calcular en la serie: "))
i = 1
sum_series = 0
while i <= lenght_serie:
    sum_series = sum_series + (i * ((i + 1) / (i + 2)))
    i += 1
print("{:.3f}".format(sum_series))
