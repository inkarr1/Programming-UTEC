sex = input("Ingresar sexo: ")
age = int(input("Ingresar edad: "))
height_cm = 100 * float(input("Ingresar altura en metros: "))

pef = (0.0448 * height_cm - 0.0304 * age + 0.35) * (sex == "M") + (0.0945 * height_cm - 0.0209 * age - 5.77) * (sex == "H")

print("EL CALCULO PEF TEORICO ES:", "{:.4f}".format(pef))