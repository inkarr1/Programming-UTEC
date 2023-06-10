import random

def create_board():
    cards = []
    values = list(range(1, 33))
    random.shuffle(values)
    for value in values:
        cards.append(Card(value))
    return cards

class Card:
    def __init__(self, value):
        self.value = value
        self.revealed = False

def print_board(board):
    for i, card in enumerate(board):
        if card.revealed:
            print(f"[ {card.value} ]", end=" ")
        else:
            print("[   ]", end=" ")
        if (i + 1) % 8 == 0:
            print()

def play_game():
    board = create_board()
    player1 = input("Ingrese el nombre del Jugador 1: ")
    player2 = input("Ingrese el nombre del Jugador 2: ")
    score = {player1: 0, player2: 0}
    turn = 1

    print_board(board)
    print(f"{player1}: {score[player1]} | {player2}: {score[player2]}")

    while any(not card.revealed for card in board):
        current_player = player1 if turn % 2 == 1 else player2
        print(f"\n--- Turno de Jugador '{current_player}' ---")
        pos1 = int(input("Posición de carta 1: "))
        pos2 = int(input("Posición de carta 2: "))

        card1 = board[pos1 - 1]
        card2 = board[pos2 - 1]

        card1.revealed = True
        card2.revealed = True

        print_board(board)

        if card1.value == card2.value:
            score[current_player] += 1
            print("¡Cartas iguales! El jugador obtiene un punto.")
        else:
            print("Las cartas no son iguales.")

        print(f"{player1}: {score[player1]} | {player2}: {score[player2]}")
        turn += 1

    if score[player1] > score[player2]:
        print(f"\n¡{player1} gana la partida!")
    elif score[player1] < score[player2]:
        print(f"\n¡{player2} gana la partida!")
    else:
        print("\n¡Empate!")

def main():
    print("Seleccione una de las siguientes opciones:")
    print("1. Registrar Jugador")
    print("2. Establecer turno")
    print("3. Iniciar Juego de Memoria")
    print("0. Salir")
    option = input("Ingrese la opción deseada: ")

    if option == "3":
        print("--- SE INICIA EL JUEGO DE MEMORIA ---")
        play_game()
    elif option == "0":
        print("¡Hasta luego!")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
