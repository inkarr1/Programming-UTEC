n = int(input("Ingrese: "))
x = 0.5
sumatoria = 0

for i in range(n):
    factorial = 1
    for j in range(2 * i + 1):
        factorial *= j + 1
    termino = ((-1) ** i) * (x ** (2 * i + 1)) / factorial
    sumatoria += termino

print(sumatoria)