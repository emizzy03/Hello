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
    best_score = -float('inf')
    best_move = None
    for col in range(7):
        row = ValidRow(board, col)
        if row is not None:
            board[row][col] = bot
            # limit the depth of the search to 3
            score = minimax(board, 0, False, 3)
            board[row][col] = ' '
            if score > best_score:
                best_score = score
                best_move = col
    if best_move is not None:
        insertLetter(bot, best_move)




def minimax(board, depth, is_maximizing, max_depth):
    if chkMarkForWin(player):
        return -1000
    if chkMarkForWin(bot):
        return 1000
    if chkDraw() or depth == max_depth:
        return evaluate(board)

    if is_maximizing:
        best_score = -float('inf')
        for col in range(7):
            row = ValidRow(board, col)
            if row is not None:
                board[row][col] = bot
                score = minimax(board, depth+1, False, max_depth)
                board[row][col] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for col in range(7):
            row = ValidRow(board, col)
            if row is not None:
                board[row][col] = player
                score = minimax(board, depth+1, True, max_depth)
                board[row][col] = ' '
                best_score = min(best_score, score)
        return best_score



def evaluate(board):
    score= 0
    center_col = [board[i][3] for i in range(6)]
    score += center_col.count(bot) * 3
    score += evaluateLines(board, bot) - evaluateLines(board, player)
    return score


def evaluateLines(board, letter):
    score = 0
    for row in range(6):
        for col in range(7):
            # Horizontal
            if col <= 3:
                score += evaluatePatterns([board[row][col+i]
                                         for i in range(4)], letter)
            # Vertical
            if row <= 2:
                score += evaluatePatterns([board[row+i][col]
                                         for i in range(4)], letter)
            # Diagonal 
            if row <= 2 and col <= 3:
                score += evaluatePatterns([board[row+i][col+i]
                                         for i in range(4)], letter)
            # Diagonal 
            if row <= 2 and col >= 3:
                score += evaluatePatterns([board[row+i][col-i]
                                         for i in range(4)], letter)
    return score



def evaluatePatterns(pattern, letter):
    opponent = player if letter == bot else bot
    score = 0
    if pattern.count(letter) == 4:
        score += 100
    elif pattern.count(letter) == 3 and pattern.count(' ') == 1:
        score += 5
    elif pattern.count(letter) == 2 and pattern.count(' ') == 2:
        score += 2
    if pattern.count(opponent) == 3 and pattern.count(' ') == 1:
        score -= 4
    return score


def ValidRow(board, col):
   for row in range(5, -1, -1):
        if board[row][col] == ' ':
            return row
   return None


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
