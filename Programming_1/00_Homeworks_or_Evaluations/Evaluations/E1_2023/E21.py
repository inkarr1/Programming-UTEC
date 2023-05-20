# Marque la alternatica correcta sobre el siguiente codigo, si el usuario ingreso 20 y 2.0

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
# Se evaluo solo la primera y lkuego la funcion retorno