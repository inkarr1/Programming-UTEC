import random

# Variables globales
jugadores = []
turnos = []
tablero = []


# Función para registrar un jugador
def registrar_jugador():
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    jugadores.append((usuario, contraseña))
    print("Jugador registrado correctamente.")


# Función para establecer el turno e iniciar el tablero
def establecer_turno_iniciar_tablero():
    global turnos
    global tablero

    if len(jugadores) == 0:
        print("Seleccione la opción 1 para registrar jugadores.")
        return

    dificultades = {
        "1": (4, 4, 8),
        "2": (4, 8, 16),
        "3": (4, 13, 26)
    }

    dificultad = input("Seleccione la dificultad del tablero (1: Fácil, 2: Normal, 3: Difícil): ")
    filas, columnas, num_cartas = dificultades.get(dificultad, (4, 4, 8))

    num_jugadores = int(input("Ingrese la cantidad de jugadores (2-4): "))

    # Validar jugadores existentes
    jugadores_validos = []
    for i in range(num_jugadores):
        usuario = input(f"Ingrese el nombre de usuario del jugador {i + 1}: ")
        contraseña = input(f"Ingrese la contraseña del jugador {i + 1}: ")
        if (usuario, contraseña) in jugadores:
            jugadores_validos.append((usuario, contraseña))
        else:
            print("Usuario o contraseña incorrectos.")
            return

    # Establecer turnos de juego
    turnos = random.sample(jugadores_validos, len(jugadores_validos))

    # Inicializar tablero
    tablero = [[0] * columnas for _ in range(filas)]
    cartas = list(range(1, num_cartas + 1)) * 2
    random.shuffle(cartas)

    # Asignar cartas al tablero
    for i in range(filas):
        for j in range(columnas):
            tablero[i][j] = cartas.pop()

    print("Turnos y tablero establecidos correctamente.")


# Función para iniciar el juego de memoria
def iniciar_juego_memoria():
    global turnos
    global tablero

    if len(turnos) == 0 or len(tablero) == 0:
        print("El turno y el tablero no han sido establecidos. Por favor, seleccione la opción 2.")
        return

    print("=== Turnos de juego ===")
    for i, jugador in enumerate(turnos, start=1):
        print(f"Turno {i}: {jugador[0]}")

    print("\n¡Comienza el juego de memoria!")

    filas = len(tablero)
    columnas = len(tablero[0])

    # Mostrar tablero con números
    print("Tablero:")
    for i in range(filas):
        for j in range(columnas):
            print(tablero[i][j], end="\t")
        print()

    jugador_actual = turnos[0]

    print(f"Turno del jugador: {jugador_actual[0]}")

    carta1 = int(input("Seleccione el número de la primera carta: "))
    carta2 = int(input("Seleccione el número de la segunda carta: "))

    # Verificar si las cartas seleccionadas son válidas
    if not (1 <= carta1 <= filas * columnas) or not (1 <= carta2 <= filas * columnas):
        print("¡Cartas inválidas! Seleccione números dentro del rango del tablero.")
        return

    # Obtener la posición de las cartas seleccionadas
    fila1 = (carta1 - 1) // columnas
    col1 = (carta1 - 1) % columnas
    fila2 = (carta2 - 1) // columnas
    col2 = (carta2 - 1) % columnas

    # Mostrar las cartas seleccionadas
    print(f"Carta {carta1}: {tablero[fila1][col1]}")
    print(f"Carta {carta2}: {tablero[fila2][col2]}")


# Función para mostrar el menú principal y procesar la opción seleccionada
def mostrar_menu_principal():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Registro de jugador")
        print("2. Establecer turno e iniciar tablero")
        print("3. Iniciar Juego de Memoria")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_jugador()
        elif opcion == "2":
            establecer_turno_iniciar_tablero()
        elif opcion == "3":
            if len(jugadores) == 0:
                print("Seleccione la opción 1 para registrar jugadores.")
            else:
                iniciar_juego_memoria()
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


# Ejecutar el programa
mostrar_menu_principal()
