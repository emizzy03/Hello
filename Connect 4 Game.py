# Name: Emmanuel Nnadi
# Date: 02/27/2024
# Assignment: create minimax connect 4 game
# define the board with 6 rows and 7 columns

# define the printBoard function to print the board
board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ']]


# function to print the board with 6 rows and 7 columns
def printBoard(board):
    print(board[0][0]+'|'+board[0][1]+'|'+board[0][2]+'|'+board[0]
          [3]+'|'+board[0][4]+'|'+board[0][5]+'|'+board[0][6])
    print('-+-+-+-+-+-+-')
    print(board[1][0]+'|'+board[1][1]+'|'+board[1][2]+'|'+board[1]
          [3]+'|'+board[1][4]+'|'+board[1][5]+'|'+board[1][6])
    print('-+-+-+-+-+-+-')
    print(board[2][0]+'|'+board[2][1]+'|'+board[2][2]+'|'+board[2]
          [3]+'|'+board[2][4]+'|'+board[2][5]+'|'+board[2][6])
    print('-+-+-+-+-+-+-')
    print(board[3][0]+'|'+board[3][1]+'|'+board[3][2]+'|'+board[3]
          [3]+'|'+board[3][4]+'|'+board[3][5]+'|'+board[3][6])
    print('-+-+-+-+-+-+-')
    print(board[4][0]+'|'+board[4][1]+'|'+board[4][2]+'|'+board[4]
          [3]+'|'+board[4][4]+'|'+board[4][5]+'|'+board[4][6])
    print('-+-+-+-+-+-+-')
    print(board[5][0]+'|'+board[5][1]+'|'+board[5][2]+'|'+board[5]
          [3]+'|'+board[5][4]+'|'+board[5][5]+'|'+board[5][6])
    print('\n')


printBoard(board)

# function to check is a certain position in the board is empty.


def spaceIsFree(row, col):
    return board[row][col] == ' '

# method to insert letter in space
# check if the last row is empty, if not, go up one row and check again, if it is empty, insert the letter there.


def insertLetter(letter, col):
    if col < 0 or col >= 7:
        print('Invalid position. Please try again.')
        return
    row = 5
    while row >= 0:
        if spaceIsFree(row, col):
            board[row][col] = letter
            printBoard(board)
            return
        row -= 1
    print('Position is full. Please pick another position.')


# function to check if board is draw
# if there are no empty spaces left, the game is a draw.
def chkDraw():
    for row in board:
        if ' ' in row:
            return False
    return True

# function to check if one user has won the game


def chkMarkForWin(letter):
    # Check rows
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] == letter:
                return True
    # Check columns
    for col in range(7):
        for row in range(3):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == letter:
                return True
    # Check diagonals
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == letter:
                return True
    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] == letter:
                return True
    return False


player = 'O'
bot = 'X'

# function for player move


def playerMove():
    position = int(input("Enter the position for 'O': "))
    insertLetter('O', position-1)
    return


def compMove():
    bestScore = -800
    best_move = 0
    for col in range(7):
        if spaceIsFree(0, col):
            row = 5
            while row >= 0:
                if spaceIsFree(row, col):
                    board[row][col] = bot
                    score = minimax(board, 0, False, 3)
                    board[row][col] = ' '
                    if score > bestScore:
                        bestScore = score
                        best_move = col
                    break
                row -= 1
    insertLetter(bot, best_move)

# limit the depth of the search to 3


def minimax(board, depth, isMaximizing, max_depth):
    if chkMarkForWin(bot):
        return 1
    if chkMarkForWin(player):
        return -1
    if chkDraw():
        return 0
    if depth == max_depth:
        return evaluate(board)
    if isMaximizing:
        bestScore = -800
        for col in range(7):
            if spaceIsFree(0, col):
                row = 5
                while row >= 0:
                    if spaceIsFree(row, col):
                        board[row][col] = bot
                        score = minimax(board, depth+1, False, max_depth)
                        board[row][col] = ' '
                        bestScore = max(score, bestScore)
                        break
                    row -= 1
        return bestScore
    else:
        bestScore = 800
        for col in range(7):
            if spaceIsFree(0, col):
                row = 5
                while row >= 0:
                    if spaceIsFree(row, col):
                        board[row][col] = player
                        score = minimax(board, depth+1, True, max_depth)
                        board[row][col] = ' '
                        bestScore = min(score, bestScore)
                        break
                    row -= 1
        return bestScore


def evaluate(board):
    # check the current state of the board and return a score
    score = 0
    # check rows
    for row in range(6):
        for col in range(4):
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] == bot:
                score += 1
            if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3] == player:
                score -= 1
    # check columns
    for col in range(7):
        for row in range(3):
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == bot:
                score += 1
            if board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col] == player:
                score -= 1
    # check diagonals
    for row in range(3):
        for col in range(4):
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == bot:
                score += 1
            if board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3] == player:
                score -= 1
    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] == bot:
                score += 1
            if board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3] == player:
                score -= 1
    return score


# main game play
while True:
    playerMove()
    if chkMarkForWin(player):
        print('Player wins!')
        break
    if chkDraw():
        print('It is a draw!')
        break
    compMove()
    if chkMarkForWin(bot):
        print('Bot wins!')
        break
    if chkDraw():
        print('It is a draw!')
