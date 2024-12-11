"""
Tic Tac Toe Game

Description:
This program is a two-player game where users take turns marking cells on a 3x3 grid, aiming to 
achieve three in a row. It provides options to replay or exit after a game ends.

Features:
- Dynamic 3x3 board display.
- Ensures valid player moves and prevents overwriting cells.
- Detects winning or tie conditions.
- Allows replay after a game ends.

How to Use:
1. Run the program.
2. Players take turns entering row and column numbers to mark their cells.
3. The game announces the winner or a tie at the end.
4. Choose to replay or exit after each game.

"""


# Function to initialize an empty 3x3 board
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Function to display the board
def display_board(board):
    print("\nCurrent Board:")
    for row in range(3):
        print(" | ".join(board[row]))
        if row < 2:
            print("-" * 5)

# Function to handle the player's move with input validation
def player_move(board, player):
    while True:
        try:
            row = int(input(f"Player {player} ({'X' if player == 1 else 'O'}), enter row (1-3): ")) - 1
            col = int(input(f"Player {player} ({'X' if player == 1 else 'O'}), enter column (1-3): ")) - 1
            if row in range(3) and col in range(3):  # Check if input is within bounds
                if board[row][col] == " ":
                    board[row][col] = "X" if player == 1 else "O"
                    break
                else:
                    print("That cell is already taken! Choose a different cell.")
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

# Function to check for a winner
def check_winner(board, player):
    symbol = "X" if player == 1 else "O"
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

# Function to check if the board is full (indicating a tie)
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Function to switch players
def switch_player(current_player):
    return 2 if current_player == 1 else 1

# Main function to run the Tic Tac Toe game
def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    while True:
        # Initialize the game
        board = initialize_board()
        current_player = 1  # Player 1 starts
        display_board(board)

        while True:
            # Player move
            player_move(board, current_player)
            display_board(board)

            # Check for a winner
            if check_winner(board, current_player):
                print(f"Player {current_player} ({'X' if current_player == 1 else 'O'}) wins! Congratulations!")
                break

            # Check for a tie
            if is_board_full(board):
                print("It's a tie!")
                break

            # Switch players
            current_player = switch_player(current_player)

        # Ask if players want to play again
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print("Thank you for playing Tic Tac Toe!")

# Uncomment the following line to run the program:
tic_tac_toe()
