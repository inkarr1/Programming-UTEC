num = int(input("Numero de alumnos"))
while (num<6 or num > 41):
    num = int(input("Numero de alumnos"))

i = 1
suma_verano = 0
sum_otono = 0
sum_invierno = 0
sum_primavera = 0

while i<=num:
    print("Fecha de nacimiento: ")
    dia = int(input("Día: "))
    mes = int(input("Mes: "))

    if mes  == 1 or mes == 2:
        suma_verano += 1
    elif mes ==  3:
        if dia < 21:
            suma_verano += 1
        else:
            sum_otono += 1
    elif mes == 4 or mes == 5:
        sum_otono += 1
    elif mes == 6:
        if dia < 22:
            sum_otono += 1
    elif mes == 10 or mes == 11:

print("Nacidos en varano", "{:.3f}".format(suma_verano/(i-1)*100))