jugadores = {}
jugadores_creados = 0


def crear_jugadores():
    user = input("\nIngrese su usuario: ")
    password = input("Ingrese su contraseña: ")

    jugadores[user] = password
    global jugadores_creados
    jugadores_creados += 1

    print(f"Usuario '{user}' creado exitosamente")


def validar_usuario():
    cantidad_jugadores = 1
    print(f"Jugador{cantidad_jugadores}")
    user = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")

    if user in jugadores and jugadores[user] == password:
        print("Acceder")
    else:
        print("""¡Datos incorrectos!
        Por favor vuelva a ingresar su usuario
        """)


def crear_tablero(filas, columnas):
    tablero = [[j + 1 + i * columnas for j in range(columnas)] for i in range(filas)]
    return tablero


def imprimir_tablero(tablero):
    for fila in tablero:
        for elemento in fila:
            print("[{:>3}]".format(elemento), end=' ')
        print()


def level_game():
    print("Seleccione Dificultad: ")
    print("""
    1. Facil
    2. Normal
    3. Dificil
    """)
    option_level = int(input("Opcion deseada: "))

    if option_level == 1:
        tablero = crear_tablero(4, 4)
        imprimir_tablero(tablero)
    elif option_level == 2:
        tablero = crear_tablero(4, 8)
        imprimir_tablero(tablero)
    elif option_level == 3:
        tablero = crear_tablero(4, 13)
        imprimir_tablero(tablero)

    validar_usuario()


def iniciar_juego():
    print("------- BIENVENIDO AL JUEGO DE MEMORIA -------")
    while True:
        print("""
Seleccione una de las siguientes opciones:
1. Registrar Jugador
2. Establecer turno
3. Iniciar Juego de Memoria
0. Salir
        """)
        option_general = int(input("Ingrese la opcion deseada: "))

        if option_general == 1:
            crear_jugadores()
        elif option_general == 2:
            if jugadores_creados < 2:
                print("Debe crear al menos dos jugadores antes de establecer el turno.")
            else:
                level_game()
        elif option_general == 3:
            print("Todavía 2")
        elif option_general == 0:
            print("Saliste del juego")
            break
        else:
            print("Opción inválida. Ingrese una opción válida.")


iniciar_juego()
