"""
Author: A H M Rezwanur Rakib Chy
Project: Tic Tac Toe Game
Instruction: Play the game on the console with python 3.6 or above.
"""

"""
An initial high level plan of the game:
- we need a board
- display that board
- play game
- handle turn
- check if there is a win
    - check rows
    - check columns
    - check diagonals
- check tie
- flip to other player
- go back and repeat the process
"""


# ----- Global Variables ----

# empty tic-tac-toe game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if game is still going, it is True by default because we want to run the loop by default initially
# It will be false only when the game is over
game_still_going = True

# Who won? Or tie? None by default because no winner right now
winner = None

# Whose turn is it
current_player = "X"


# display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    # print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    # print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# function to drive the tic tac toe game
def play_game():

    # display initial board
    display_board()
    """we want to have a loop that turns over and over again
    between X and O until somebody win or there is a tie"""
    while game_still_going:

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # if the game isn't over, flip one player to other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " wins. Congratulations!")
    elif winner == None:
        print("Tie.")


# handle a single turn of a random player
def handle_turn(player):
    print("now " + player + "'s turn.")
    # get the position of the player
    position = input("Choose a position from 1-9: ")

    # validation part
    valid = False
    while not valid:

        # input validation (could use a regular expression)
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        # converted position to int and subtracted one to get correct index
        position = int(position) - 1

        # check if the position we picked valid on the board
        if board[position] == "-":
            valid = True
        else:
            print("Invalid board position! You can't go there, try again!")

    # to put something in the board
    board[position] = player

    display_board()


def check_if_game_over():
    # it calls two other functions
    check_for_winner()
    check_if_tie()


def check_for_winner():

    # Set up global variables
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonal
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        # there was no win
        winner = None


def check_rows():
    # set up global variables
    global game_still_going
    # check if any of the rows have all the same value (and is not equal)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner (X or O)
    # Following are first elements of the rows
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


def check_columns():
    # set up global variables
    global game_still_going
    # check if any of the columns have all the same value (and is not equal)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner (X or O)
    # following are first element of the columns
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # set up global variables
    global game_still_going
    # check if any of the columns have all the same value (and is not equal)
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"
    # If any diagonals does have a match, flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
    # Return the winner (X or O)
    # following are first element of the columns
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return


# function to execute when there is a tie
def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


# function to flip the player from X to O
def flip_player():
    # global variables we need
    global current_player
    # if the current player was X, then change to O
    if current_player == "X":
        current_player = "O"
    # if the current player was O, then change to X
    elif current_player == "O":
        current_player = "X"


# following code executes the game function
play_game()
