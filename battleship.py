"""
Programmed by Ethan Cha
Made using Python 2
"""

from random import randint

# making the board
board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

# Selecting random enemy ship location
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Player events
for turn in range(5):
    print "Turn", turn + 1
    guess_row = int(raw_input("Guess Row:")) - 1
    guess_col = int(raw_input("Guess Col:")) - 1

    if guess_row == ship_row and guess_col == ship_col:
        board[guess_row][guess_col] = "*"
        print_board(board)
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif (board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    print_board(board)
else:
    print "Game Over"
    print "Ship Row:", ship_row + 1
    print "Ship Col:", ship_col + 1