print("Fecha de nacimiento")
day_birth = int(input("Día: "))
month_birth = int(input("Mes: "))
year_birth = int(input("Año: "))

print("Fecha actual")
day_now = int(input("Día: "))
month_now = int(input("Mes: "))
year_now = int(input("Año: "))

age = year_now - year_birth

if month_now < month_birth:
    age -= 1
elif month_now == month_birth:
    if day_now < day_birth:
        age -= 1

print("Su edad es:", age)
if age < 13:
    print("Su generación aun no tiene nombre asignado.")
elif age < 21:
    print("Su generación es la Generación Z.")
elif age < 36:
    print("Su generación es la Generación Y.")
elif age < 60:
    print("Su generación es la Generación X.")
else:
    print("Su generación es la Generación Baby Boomers.")