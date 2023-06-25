def pregunta_2(
        Dic: list[dict],
        valor: int,
        low: int = 0,
        high: int = None
) -> dict:
    resultado = {}
    # Codigo para Pregunta 2 comienza aqui

    if high is None:
        high = len(Dic) - 1

    while low <= high:
        mid = (low + high) // 2
        if Dic[mid]['id'] == valor:
            resultado = Dic[mid]
            break
        elif Dic[mid]['id'] < valor:
            low = mid + 1
        else:
            high = mid - 1

    # Codigo par Pregunta 2 termina aquí. Recuerda almacenar el resultado en la variable resultado.
    return resultado