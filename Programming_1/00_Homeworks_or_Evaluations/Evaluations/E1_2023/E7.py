# Si el usuario ingresa por teclado -1 ?Que imprimira por
# pantalla el siguiente codigo?

x = int(input())
if 0 <= x <= 10:
    print("s/10")
elif 11 <= x <= 20:
    print("s/15.0")
else:
    print("s/20.0")
