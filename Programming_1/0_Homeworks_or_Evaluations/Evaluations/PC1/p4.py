numero_serie = int(input("Ingrese la cantidad de terminos: "))
i_contador = 0
n_numero = 1
resultado_serie = 0

while i_contador < numero_serie:
    if n_numero % 2 == 0:
        total = n_numero ** 2 * -1
    else:
        total = n_numero ** 2
    resultado_serie = resultado_serie + total
    i_contador += 1
    n_numero += 1
    print(f"{i_contador}. {resultado_serie}")