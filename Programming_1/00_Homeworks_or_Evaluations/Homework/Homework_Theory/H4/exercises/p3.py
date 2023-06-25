def pregunta_3(
        Dic: list[dict],
        funcion: str,
        col_name: str,
        valor: str,
        ord_type: str
) -> list[dict]:
    resultado = []
    # Codigo para Pregunta 3 comienza aqui

    if funcion == 'Busqueda':
        for libro in Dic:
            if libro[col_name] == valor:
                resultado.append(libro)

    elif funcion == 'Clasificacion':
        if ord_type == 'asc':
            Dic.sort(key=lambda x: x[col_name])
        elif ord_type == 'desc':
            Dic.sort(key=lambda x: x[col_name], reverse=True)
        resultado = Dic

    # Codigo par Pregunta 3 termina aquí. Recuerda almacenar el resultado en la variable resultado.
    return resultado

