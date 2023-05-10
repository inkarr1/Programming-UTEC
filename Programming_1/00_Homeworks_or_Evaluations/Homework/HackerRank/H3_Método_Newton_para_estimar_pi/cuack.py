range_input = int(input("Ingrese rango: "))
suma = 0


for y in range(1, range_input+1):
    for i in range(range_input):
        series_multi = ((2 * i) + 1) / ((2 * i) + 2)
        print("i", i, ":", series_multi)
    series_expo = ((1 / 2) ** ((2 * y) + 1)) / ((2 * y) + 1)
    print("y", y, ":", series_expo)
    series_result = series_multi * series_expo

    suma = suma + series_result
pi = 6 * ((1 / 2) + suma)
print("resultado", pi)