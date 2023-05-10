x = int(input("Ingresa: "))

i = 0
result_series = 1

y = 1
sumatoria = 0

while y <= x:
    while i < x:
        series_multi = ((2 * i) + 1) / ((2 * i) + 2)
        result_series = result_series * series_multi
        i += 1
    solution = result_series * ((1/2) / ((2 * y) + 1))
    y += 1
print(6*(1/2 + solution))


