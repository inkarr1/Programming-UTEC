n_consume = int(input("Consumo: "))
percent_waiter = 5/100
percent_igv = 18/100

total_paid_consume = n_consume + (n_consume * (percent_waiter + percent_igv))

print("El monto a pagar es", total_paid_consume)