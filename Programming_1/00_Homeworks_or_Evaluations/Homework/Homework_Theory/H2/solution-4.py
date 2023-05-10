# NO MODIFICAR NADA BAJO ESTA LINEA
class main:
    # NO MODIFICAR NADA SOBRE ESTA LINEA

    # ============Pregunta 1=================
    @staticmethod
    def pregunta_1(N: int, M: int) -> str:
        resultado = ""
        # Codigo para Pregunta 1 comienza aqu
        if N > M:
            N, M = M, N

        for i in range(N, M + 1):
            for j in range(1, 11):
                resultado = i * j

        # Codigo para Pregunta 1 acaba aqui. Recuerda almacenar el resultado en la variable resultado.        
        return resultado

    # ============Pregunta 2=================
    @staticmethod
    def pregunta_2(contrasenas: str) -> str:
        cantidad_validas = 0
        cantidad_invalidas = 0
        lista_validas = []
        # Codigo para Pregunta 2 comienza aqui


    
        # Codigo par Pregunta 2 termina aquí. Recuerda almacenar el resultado en la variable resultado.
        return cantidad_validas, cantidad_invalidas, lista_validas
    
    # ============Pregunta 3=================
    @staticmethod
    def pregunta_3(N: int, mensaje: str, S: str) -> str:
        mensaje_encriptado = ""
        # Codigo para Pregunta 3 comienza aqui
        
        
        
        # Codigo par Pregunta 3 termina aquí. Recuerda almacenar el resultado en la variable resultado.
        return mensaje_encriptado

# NO MODIFICAR NADA BAJO ESTA LINEA
if __name__ == '__main__':
    main()
# NO MODIFICAR NADA SOBRE ESTA LINEA
