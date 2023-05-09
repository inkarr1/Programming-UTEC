n_bottles_minor_liter = int(input("Numero de botellas de hasta un litro: "))
n_bottle_major_liter = int(input("Numero de botellas de mas de un litro: "))

money_minor_liter = n_bottles_minor_liter * 1.25
money_major_liter = n_bottle_major_liter * 3.75

total_money = money_minor_liter + money_major_liter

print("El monto a favor es de", total_money)