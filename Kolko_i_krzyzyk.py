
from re import split
import random


def main():
    who_won = 2   
    board = game_setup()
    print_board(board)
    
    while who_won > 1:
        while True:
            r, c = user_input()
            if board[r][c] == "X" or board[r][c] == "O" :
                continue
            else:
                break
        board[r][c] = "O"
        print_board(board)
        if check_win(board) == 1:
            who_won = 0
            break
        
        board = computer_move(board)
        print_board(board)
        if check_win(board) == 1:
            who_won = 1

    if who_won == 0:
        print("You won!!!! I will get you next time.")
    elif who_won == 1:
        print("You lost!!! Better luck next time")

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
    board[1][1] = "X"
    print("Lets play tic-tac-toe !!!\nI will start")
    return board

def check_win(board):

    counter = 0

    def win_con(x):
        if x == 2:
            return 1
        else: 
            x = 0
            return 0

    for i in range(3):
        for j in range(2):
            if board[i][j] != " " and board[i][j] == board[i][j+1]:
                counter += 1

        if win_con(counter) == 1:
            return 1
        else:
            counter = 0
            

    for i in range(2):
        for j in range(3):
            if board[i][j] != " " and board[i][j] == board[i-1][j]:
                counter += 1

        if win_con(counter) == 1:
            return 1
        else:
            counter = 0

    if board[0][0] == board[1][1] == board[2][2] or board[0][2]==board[1][1]==board[2][0]:
        return 1

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

main()


