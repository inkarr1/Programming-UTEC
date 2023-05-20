# Marque la alternativa correcta sobre el siguiente codigo, si el
# usuario ingres 10 y 2.0 respectivamente

def f():
    edad = int(input())
    altura = float(input())

    if edad > 18 and altura >= 2.0:
        print("1")
        return

    if edad > 18 and altura < 2.0:
        print("2")
        return

    if edad < 18:
        print("3")
        return


f()
# Se evaluo todas las condiciones

