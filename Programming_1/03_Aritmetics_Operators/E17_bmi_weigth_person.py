weigth = int(input("Ingrese el peso en grs: "))
height = int(input("Ingrese la altura en cms: "))

bmi = (weigth / 1000) / (height / 100) ** 2

print("El índice de masa corporal (BMI) es igual a: ", "{:.3f}".format(bmi))