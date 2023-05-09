consume = int(input("Kw: "))

result = (consume <= 100) * (0.4522 * consume)
result = result + (consume > 100) * (100 * 0.4522 + (consume - 100) * 0.7)


print("El monto a pagar es: ", str(result))