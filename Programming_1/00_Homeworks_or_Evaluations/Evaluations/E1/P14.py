def f():
    edad = int(input()) #20
    altura = float(input()) #1.8

    # primera iteracion
    if edad > 18 and altura > 2.0:
        print('a')
        return

    # segunda iteracion
    if edad > 18 and altura < 2.0:
        print('b')
        return

    #tercera iteracion
    if edad < 18:
        print('c')
        return

f()