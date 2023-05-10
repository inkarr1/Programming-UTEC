n = int(input("Ingrese: "))

result = n
series = n

for x in range(1, 50):
    series = series * ((((2 * x) - 1) ** 2) * (n ** 2)) / (2 * x * ((2 * x) + 1))
    result += series

print(result)
