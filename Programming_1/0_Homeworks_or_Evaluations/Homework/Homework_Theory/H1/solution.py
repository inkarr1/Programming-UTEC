
# NO MODIFICAR NADA BAJO ESTA LINEA
def main():
    # NO MODIFICAR NADA SOBRE ESTA LINEA

    # ============Pregunta 1============
    N = str(input('N: '))

    # Tu solución inicia aquí

    if len(N) <= 5:
        print(N.upper())
    else:
        print(N.lower())
    # Tu solución termina aquí. Recuerda imprimir el resultado final. NO DEJES EL PRINT VACÍO.

    # ============Pregunta 2============
    N = int(input('N: '))

    # Tu solución inicia aquí
    if N % 2 == 0:
        print('par')
    else:
        print('impar')

    # Tu solución termina aquí. Recuerda imprimir el resultado final. NO DEJES EL PRINT VACÍO.

    # ============Pregunta 3============
    N = int(input('N: '))

    # Tu solución inicia aquí
    result = ((N % 3 == 1) * "no ") + "es multiplo de 3"
    print(result)

    # Tu solución termina aquí. Recuerda imprimir el resultado final. NO DEJES EL PRINT VACÍO.

    # ============Pregunta 4============
    N = int(input('N: '))
    M = int(input('N: '))

    # Tu solución inicia aquí
    print(f'es multiplo de {M}' if N % M == 0 else f'no es multiplo de {M}')

    # Tu solución termina aquí. Recuerda imprimir el resultado final. NO DEJES EL PRINT VACÍO.

    # ============Pregunta 5============
    N = int(input('N: '))

    # Tu solución inicia aquí
    if N % 5 == 0 and N % 7 == 0:
        print("es multiplo de 7 y de 5")
    elif N % 5 == 0:
        print("es multiplo de 5 pero no de 7")
    elif N % 7 == 0:
        print("es multiplo de 7 pero no de 5")
    else:
        print("no es multiplo de 7 ni de 5")

    # Tu solución termina aquí. Recuerda imprimir el resultado final. NO DEJES EL PRINT VACÍO.


# NO MODIFICAR NADA BAJO ESTA LINEA
if __name__ == '__main__':
    main()
# NO MODIFICAR NADA SOBRE ESTA LINEA
