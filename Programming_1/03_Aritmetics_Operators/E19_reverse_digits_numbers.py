num = int(input("Numero: "))

while num >= 1:
    num_rpta = num % 10
    num = num // 10
    result = num_rpta

print("Numero invertido:", result)