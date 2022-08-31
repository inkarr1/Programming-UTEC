# Escribir un programa que permita ingresar 3 edades e indique cuál es el mayor

age_1 = int(input("Ingrese la primera edad: "))
age_2 = int(input("Ingrese la segunda edad: "))
age_3 = int(input("Ingrese la tercera edad: "))

if age_1 > age_2 and age_1 > age_3:
    print(f"{age_1} es la edad mayor")
elif age_2 > age_1 and age_2 > age_3:
    print(f"{age_2} es la edad mayor")
elif age_3 > age_1 and age_3 > age_2:
    print(f"{age_3} es la edad mayor")