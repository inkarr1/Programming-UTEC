def initialize_board():
    board = [['[.]' for _ in range(9)] for _ in range(9)]
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def place_ship(board, row, col, size, orientation):
    for i in range(size):
        if orientation == 0:
            board[row + i][col] = '[B]'
        else:
            board[row][col + i] = '[B]'

def make_shot(board, row, col):
    if board[row][col] == '[B]':
        board[row][col] = '[X]'
    else:
        board[row][col] = '[O]'

board = initialize_board()

for _ in range(2):
    row = int(input())
    col = int(input())
    size = int(input())
    orientation = int(input())
    place_ship(board, row, col, size, orientation)

print_board(board)

row = int(input())
col = int(input())
make_shot(board, row, col)

print_board(board)

