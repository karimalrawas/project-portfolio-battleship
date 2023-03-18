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

# Welcome message
print("Welcome to Battleship of Destiny!")
print("Sink all three ships to defeat the AI and save humanity!")

# Place ships on the board
ships = place_ships(3)

# Track scores
player_score = 0
computer_score = 0

# Looping the game 
turns = 0
while True:
    print("\nTurn:", turns+1)
    print_board(board)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    # Player's turn
    if (guess_row, guess_col) in ships:
        print("Hurray! You sunk a battleship!")
        board[guess_row][guess_col] = "S"
        ships.remove((guess_row, guess_col))
        player_score += 1
        if not ships:
            print("\nCongratulations! You won!")
            print("Player score:", player_score)
            print("Computer score:", computer_score)
            break
    else:
        if guess_row not in range(5) or \
            guess_col not in range(5):
            print("Nice try, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You've tried this already.")
        else:
            print("You missed human!")
            board[guess_row][guess_col] = "X"
        print("Player score:", player_score)
        print("Computer score:", computer_score)

    # Computer's turn
    computer_guess_row = random.randint(0, len(board) - 1)
    computer_guess_col = random.randint(0, len(board[0]) - 1)
    if (computer_guess_row, computer_guess_col) in ships:
        print("\nThe computer sunk one of your battleships!")
        board[computer_guess_row][computer_guess_col] = "C"
        ships.remove((computer_guess_row, computer_guess_col))
        computer_score += 1
        if not ships:
            print("\nGame over. The computer won!")
            print("Player score:", player_score)
            print("Computer score:", computer_score)
            break
    else:
        print("\nThe computer missed your battleship!")
        board[computer_guess_row][computer_guess_col] = "X"
    print("Player score:", player_score)
    print("Computer score:", computer_score)

    turns += 1
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

# Welcome message
print("Welcome to Battleship!")
print("Try to sink all three battleships in as few turns as possible.")

# Place ships on the board
ships = place_ships(3)

# Track scores
player_score = 0
computer_score = 0

# Looping the game 
turns = 0
while True:
    print("\nTurn:", turns+1)
    print_board(board)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    # Player's turn
    if (guess_row, guess_col) in ships:
        print("Congratulations! You sunk a battleship!")
        board[guess_row][guess_col] = "S"
        ships.remove((guess_row, guess_col))
        player_score += 1
        if not ships:
            print("\nCongratulations! You won!")
            print("Player score:", player_score)
            print("Computer score:", computer_score)
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
        print("Player score:", player_score)
        print("Computer score:", computer_score)

    # Computer's turn
    computer_guess_row = random.randint(0, len(board) - 1)
    computer_guess_col = random.randint(0, len(board[0]) - 1)
    if (computer_guess_row, computer_guess_col) in ships:
        print("\nThe computer sunk one of your battleships!")
        board[computer_guess_row][computer_guess_col] = "C"
        ships.remove((computer_guess_row, computer_guess_col))
        computer_score += 1
        if not ships:
            print("\nGame over. The computer won!")
            print("Player score:", player_score)
            print("Computer score:", computer_score)
            break
    else:
        print("\nThe computer missed your battleship!")
        board[computer_guess_row][computer_guess_col] = "X"
    print("Player score:", player_score)
    print("Computer score:", computer_score)

    turns += 1
