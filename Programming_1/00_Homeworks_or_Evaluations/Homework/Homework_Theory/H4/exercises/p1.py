def pregunta_1(
        Dic: list[dict],
        col_name: str,
        ord_type: str
) -> list[dict]:
    resultado = Dic
    # Codigo para Pregunta 1 comienza aqui

    for i in range(len(resultado)):
        min_idx = i
        for j in range(i + 1, len(resultado)):
            if (ord_type == 'asc' and resultado[j][col_name] < resultado[min_idx][col_name]) or \
                     (ord_type == 'desc' and resultado[j][col_name] > resultado[min_idx][col_name]):
                min_idx = j

        resultado[i], resultado[min_idx] = resultado[min_idx], resultado[i]

    # Codigo para Pregunta 1 acaba aqui. Recuerda almacenar el resultado en la variable resultado.
    return resultado


Dic = [
    {'id': 6, 'descripcion': 'Tarea 6', 'importancia': 6},
    {'id': 2, 'descripcion': 'Tarea 2', 'importancia': 2},
    {'id': 5, 'descripcion': 'Tarea 5', 'importancia': 5},
    {'id': 4, 'descripcion': 'Tarea 4', 'importancia': 4},
    {'id': 3, 'descripcion': 'Tarea 3', 'importancia': 3},
    {'id': 1, 'descripcion': 'Tarea 1', 'importancia': 1},
]

col_name = input("id: ")
ord_type = input("order: ")

result = pregunta_1(Dic, col_name, ord_type)
print(result)
