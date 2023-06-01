def pregunta_3(N: int, mensaje: str, S: str) -> str:
    mensaje_encriptado = ""
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    mensaje = mensaje.lower()

    for letra in mensaje:
        if letra in abecedario:
            indice = abecedario.index(letra)
            nueva_letra = S[indice]
            nueva_posicion = (S.index(nueva_letra) + N) % 26
            mensaje_encriptado += S[nueva_posicion]
        else:
            mensaje_encriptado += letra

    return mensaje_encriptado


N = int(input("N: "))
mensaje = input("mensaje: ")
S = input("S: ")

print(pregunta_3(N, mensaje, S))
