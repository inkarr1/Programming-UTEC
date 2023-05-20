def pregunta_1(N: int, M: int) -> str:
    resultado = ""
    # Codigo para Pregunta 1 comienza aqui

    # Codigo para Pregunta 1 acaba aqui. Recuerda almacenar el resultado en la variable resultado.
    return resultado


N = int(input("N: "))
M = int(input("M: "))

if N > M:
    N, M = M, N

for i in range(N, M + 1):
    for j in range(1, 11):
        resultado = i * j
        print(resultado)
