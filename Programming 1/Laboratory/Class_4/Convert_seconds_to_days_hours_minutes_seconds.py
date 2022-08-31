num = int(input("Ingrese los segundos: "))

days = num//(24*60*60)
num = num%(24*60*60)

hours = num//(60*60)
num = num%(60*60)

minutes = num//(60)
seconds = num%(60)

print("Equivale a: ", days, ":", hours, ":", minutes, ":", seconds)