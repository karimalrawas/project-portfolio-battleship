import random

# Game board size 
board = []
for x in range(5):
    board.append(["O"] * 5)

# Print game board for deplyoment 
def print_board(board):
    for row in board:
        print(" ".join(row))

# Ships symbols and placement on the board
def place_ships(num_ships):
    ships = []
    for i in range(num_ships):
        ship_row = random.randint(0, len(board) - 1)
        ship_col = random.randint(0, len(board[0]) - 1)
        ships.append((ship_row, ship_col))
    return ships

ships = place_ships(3)

# Looping the game 
turns = 0
while True:
    print("Turn:", turns+1)
    print_board(board)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if (guess_row, guess_col) in ships:
        print("Congratulations! You sunk a battleship!")
        board[guess_row][guess_col] = "S"
        ships.remove((guess_row, guess_col))
        if not ships:
            print("Congratulations! You won!")
            break
    else:
        if guess_row not in range(5) or \
            guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed the battleship!")
            board[guess_row][guess_col] = "X"

    turns += 1

