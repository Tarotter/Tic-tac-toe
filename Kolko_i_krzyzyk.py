
from re import split


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
        check_win(board)


        




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
    return row, column

def game_setup():
    board = [[" " for i in range(3)] for j in range(3)]
    board[1][1] = "x"
    print("Lets play tic-tac-toe !!!\nI will start")
    return board

def check_win(board):


    def win_con(x):
        if x == 2:
            return 1
        else: 
            x = 0
            return 0

    for i in range(3):
        for j in range(2):
            if board[i][j] is not " " and board[i][j] == board[i][j+1]:
                win_con += 1

        if win_con(win_con) == 1:
            break

    for i in range(2):
        for j in range(3):
            if board[i][j] is not " " and board[i][j] == board[i-1][j]:
                win_con += 1

        if win_con(win_con) == 1:
            break

    for i in range(2):
        for j in range(2):
            if board[i][j] is not " " and board[i][j] == board[i+1][j+1]:
                win_con += 1

        if win_con(win_con) == 1:
            break