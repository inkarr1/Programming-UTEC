def pregunta_1(N, M) -> str:
    resultado = ""

    if N > M:
        N = M
        M = N

    for i in range(N, M + 1):
        for j in range(1, 11):
            resultado += str(i * j)
            if j != 10:
                resultado += " "
        resultado += "\n"

    return resultado

N = int(input("N: "))
M = int(input("M: "))

print(pregunta_1(N, M))
