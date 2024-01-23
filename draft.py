import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)
    print()

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def player_move(board, player):
    print_board(board)

    if player == 'X':
        row = int(input(f"Player {player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, or 2): "))
    else:
        row, col = bot_move(board)

    if board[row][col] != ' ':
        print("Cell already taken. Try again.")
        return player_move(board, player)

    board[row][col] = player

    if check_winner(board, player):
        print_board(board)
        print(f"Player {player} wins!")
        return True

    if is_board_full(board):
        print_board(board)
        print("It's a tie!")
        return True

    return False

def bot_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        if player_move(board, current_player):
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()