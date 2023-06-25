def sort(data, reverse=True):
    return "clear"

def sorted(data, reverse=True):
    return "clear"
#NO MODIFICAR NADA ENCIMA DE ESTA LÍNEA

class main():
    def pregunta_1(
            Dic: list[dict],
            col_name: str,
            ord_type: str
        )-> list[dict]:
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

    # ============Pregunta 2=================
    def pregunta_2 (
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

    # ============Pregunta 3=================
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
