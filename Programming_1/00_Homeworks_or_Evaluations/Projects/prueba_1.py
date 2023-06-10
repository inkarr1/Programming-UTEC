import random

# Función para crear el tablero con cartas aleatorias
def crear_tablero():
    cartas = ["A", "B", "C", "D", "E", "F", "G", "H"] * 2
    random.shuffle(cartas)
    tablero = [cartas[i:i+4] for i in range(0, 16, 4)]
    return tablero

# Función para mostrar el tablero actual
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# Función principal del juego
def jugar():
    tablero = crear_tablero()
    mostrar_tablero(tablero)
    pares_encontrados = []
    intentos = 0

    while len(pares_encontrados) < 8:
        intentos += 1
        print(f"\nIntento #{intentos}")
        fila1 = int(input("Ingrese el número de fila de la primera carta: "))
        col1 = int(input("Ingrese el número de columna de la primera carta: "))
        carta1 = tablero[fila1][col1]

        fila2 = int(input("Ingrese el número de fila de la segunda carta: "))
        col2 = int(input("Ingrese el número de columna de la segunda carta: "))
        carta2 = tablero[fila2][col2]

        if (fila1, col1) == (fila2, col2):
            print("No puede seleccionar la misma carta dos veces.")
            continue

        if carta1 == carta2 and (fila1, col1) not in pares_encontrados:
            print("¡Encontraste un par!")
            pares_encontrados.append((fila1, col1))
            pares_encontrados.append((fila2, col2))
        else:
            print("No es un par válido.")

        mostrar_tablero(actualizar_tablero(tablero, pares_encontrados))

    print(f"\n¡Felicidades! Completaste el juego en {intentos} intentos.")

# Función para actualizar el tablero mostrando las cartas encontradas
def actualizar_tablero(tablero, pares_encontrados):
    tablero_actualizado = []
    for fila in tablero:
        nueva_fila = []
        for carta in fila:
            nueva_fila.append(carta if carta in pares_encontrados else "X")
        tablero_actualizado.append(nueva_fila)
    return tablero_actualizado

# Iniciar el juego
jugar()
