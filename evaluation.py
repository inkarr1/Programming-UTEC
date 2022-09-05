sexo = input("Ingresar sexo: ")
age = int(input("Ingresar edad: "))
height = float(input("Ingresar altura en metros: "))

new_height = height * 100

pef = (0.0448 * new_height - 0.0304 * age + 0.35) * (sexo == "M") + (0.0945 * new_height - 0.0209 * age - 5.77) * (sexo == "H")

print("EL CALCULO PEF TEORICO ES:", "{:.4f}".format(pef))