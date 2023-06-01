# NO MODIFICAR NADA BAJO ESTA LINEA
class main:
    # NO MODIFICAR NADA SOBRE ESTA LINEA

    # ============Pregunta 1=================
    @staticmethod
    def pregunta_1(N: int, M: int) -> str:
        resultado = ""
        # Codigo para Pregunta 1 comienza aqui

        if N > M:
            N, M = M, N

        for i in range(N, M + 1):
            for j in range(1, 11):
                resultado += str(i * j)
                if j != 10:
                    resultado += " "
            resultado += "\n"

        # Codigo para Pregunta 1 acaba aqui. Recuerda almacenar el resultado en la variable resultado.        
        return resultado

    # ============Pregunta 2=================
    #@staticmethod
    def pregunta_2(contrasenas: str) -> str:
        cantidad_validas = 0
        cantidad_invalidas = 0
        lista_validas = []
        # Codigo para Pregunta 2 comienza aqui

        contrasenas = contrasenas.split("/")

        caracteres_especiales = ["-", "*", "?", "!", "@"]

        for contrasena in contrasenas:
            if len(contrasena) < 8:
                cantidad_invalidas += 1
                continue

            if not any(letra.isupper() for letra in contrasena):
                cantidad_invalidas += 1
                continue
            if not any(letra.islower() for letra in contrasena):
                cantidad_invalidas += 1
                continue
            if not any(letra in caracteres_especiales for letra in contrasena):
                cantidad_invalidas += 1
                continue

            if " " in contrasena:
                cantidad_invalidas += 1
                continue

            cantidad_validas += 1

            lista_validas.append(contrasena)
    
        # Codigo par Pregunta 2 termina aquí. Recuerda almacenar el resultado en la variable resultado.
        return cantidad_validas, cantidad_invalidas, lista_validas
    
    # ============Pregunta 3=================
    @staticmethod
    def pregunta_3(N: int, mensaje: str, S: str) -> str:
        mensaje_encriptado = ""
        # Codigo para Pregunta 3 comienza aqui
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
        
        
        # Codigo par Pregunta 3 termina aquí. Recuerda almacenar el resultado en la variable resultado.
        return mensaje_encriptado

# NO MODIFICAR NADA BAJO ESTA LINEA
if __name__ == '__main__':
    main()
# NO MODIFICAR NADA SOBRE ESTA LINEA
