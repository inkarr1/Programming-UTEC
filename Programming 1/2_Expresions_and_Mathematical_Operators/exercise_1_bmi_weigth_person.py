# Desarrolle un programa que permita leer el peso de una persona expresado en gramos,
# la altura expresada en centímetros y el programa calcule el índice de masa corporal.

# El índice de la masa corporal, de las siglas en inglés BMI se calcula utilizando la siguiente fórmula:

# BMI = peso(Kg) / altura(m) * altura(m)

weigth = int(input("Ingrese el peso en grs: "))
height = int(input("Ingrese la altura en cms: "))

bmi = (weigth / 1000) / (height / 100) ** 2

print("El índice de masa corporal (BMI) es igual a: ", "{:.4f}".format(bmi))