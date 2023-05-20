n_range = int(input("Ingrese cuantos numeros desea calcular en la serie: "))
output_result = 0

for i in range(1, n_range + 1):
    n_serie = i * (i + 1) / (i + 2)

    if i % 2 == 0:
        output_result -= n_serie
    else:
        output_result += n_serie

print("{:.3f}".format(output_result))


