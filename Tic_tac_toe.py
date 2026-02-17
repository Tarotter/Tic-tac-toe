
from re import split
import random

def main():
    game()

    while True:
        rematch =  input("Type 'yes' for rematch, 'no' to end: ")
        if rematch == 'yes':
            game()
        elif rematch == 'no':
            return 0


def game():
    check = 2   
    board = game_setup()
    print_board(board)
    
    while True:

        # User input
        while True:
            r, c = user_input()
            if board[r][c] == "X" or board[r][c] == "O" :
                continue
            else:
                break

        # User moves
        board[r][c] = "O"
        print_board(board)

        # Check for win
        if check_win(board) == 1:
            check = 0
            break
        elif check_win(board) == 2:
            check = 2
            break
        
        # Computer moves
        board = computer_move(board)
        print_board(board)
        
        # Check for win
        if check_win(board) == 1:
            check = 1
            break
        elif check_win(board) == 2:
            check = 2
            break


    # Print score
    print_score(check)
    return 0

def print_board(board):
    for i in range (3):
        for j in range(3):
            print (f"| {board[i][j]} |", end = '')
        print()
    print()

def user_input():
    temp = input("Row Column: ")
    row, column = temp.split()
    print()
    return int(row), int(column)

def game_setup():
    board = [[" " for i in range(3)] for j in range(3)]
    board = computer_move(board)
    print("Lets play tic-tac-toe !!!\nI will start")
    return board

def check_win(board):

    counter = 0

    # Rows
    for i in range(3):
        for j in range(2):
            if board[i][j] != " " and board[i][j] == board[i][j+1]:
                counter += 1

        if counter == 2:
            return 1
        else:
            counter = 0
            
    # Columns
    for i in range(2):
        for j in range(3):
            if board[i][j] != " " and board[i][j] == board[i+1][j]:
                counter += 1

        if counter == 2:
            return 1
        else:
            counter = 0

    # Diagonal
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2]==board[1][1]==board[2][0] != ' ':
        return 1

    # Check for draw
    op = 0
    for row in board:
        for i in row:
            if i == ' ':
                op = 1
                break
    if op == 0:
        return 2

    return 0

def computer_move(board):
    
    while True:
        x = random.randint(0,2)
        y = random.randint(0,2)
        if board[x][y] != ' ':
            continue
        else:
            board[x][y] = 'X'
            break
    return board

def print_score(x):
    if x == 0:
        print("You won!!! I will get you next time.")
    elif x == 1:
        print("You lost!!! Better luck next time")
    elif x == 2:
        print("Draw!!")

main()


