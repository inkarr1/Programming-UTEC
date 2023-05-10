n = int(input("Ingrese el valor de n: "))
result = 0

for i in range(1, n+1):

    if i % 2 == 0:
        operation = 2 / (7 ** i)
    else:
        operation = 1 / (7 ** i)

    result = result + operation

print(f"Aproximacion con n={n} para 3/16:", "{:.17f}".format(result))