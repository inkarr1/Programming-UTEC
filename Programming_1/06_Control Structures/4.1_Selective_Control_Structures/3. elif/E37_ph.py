ph = int(input("PH: "))

if ph>=0 and ph<=1:
    print("Muy ácido")
elif ph<5:
    print("Moderadamente ácido")
elif ph<7:
    print("Ligeramente ácido")
elif ph<8:
    print("Neutro")
elif ph < 10:
    print("Ligeramente básico")
elif ph < 13:
    print("Moderadamente básico")
elif ph < 15:
    print("Muy básico")
else:
    print("El valor esta fuera del rango")

print("Gracias por usar el programa!.")