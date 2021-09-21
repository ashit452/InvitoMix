board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def choose(val):
    global p1 ,p2
    if val=='X' or val=='x':
        p1='X'
        p2='O'
    elif val=='O' or val=='o':
        p1 = 'O'
        p2 = 'X'
    else:
        print("Choose from (x/o)")
        i = input("Choose (x/o):")
        choose(i)

def printBoard(board):
    print(" " + board[0] + "| " + board[1] + "| " + board[2])
    print("---------")
    print(" " + board[3] + "| " + board[4] + "| " + board[5])
    print("---------")
    print(" " + board[6] + "| " + board[7] + "| " + board[8])


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == " "


def isWinner(bo, le):
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or
            (bo[3] == le and bo[4] == le and bo[5] == le) or
            (bo[0] == le and bo[1] == le and bo[2] == le) or
            (bo[0] == le and bo[3] == le and bo[6] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[0] == le and bo[4] == le and bo[8] == le) or
            (bo[2] == le and bo[4] == le and bo[6] == le))
def player1Move():
    run = True
    while run:
        print("Player1's turn")
        move = int(input("Please select a position to place an " + p1 + "(1-9): "))
        try:
            move = move - 1
            if move >= 0 and move <= 9 :
                if spaceIsFree(move):
                    run = False
                    insertLetter(p1, move)
                else:
                    print("Sorry this space is occupied")
            else:
                print("Please type the number within the range")
        except:
            print("Please type a number. ")


def player2Move():
    run = True
    while run:
        print("Player2's turn")
        move = int(input("Please select a position to place an " + p2 + "(1-9): "))
        try:
            move = move-1
            if move >= 0 and move <= 9:
                if spaceIsFree(move):
                    run = False
                    insertLetter(p2, move)
                else:
                    print("Sorry this space is occupied")
            else:
                print("Please type the number within the range")
        except:
            print("Please type a number. ")

def aiMove():
    run = True
    while run:
        print("AI's turn")
        move = board.count(" ")
        if spaceIsFree(move):
            run = False
            insertLetter(p2, move)
        else:
            move = board.count(" ")-1
            if spaceIsFree(move):
                run = False
                insertLetter(p2, move)


def isBoardFull(board):
    if board.count(" ") > 0:
        return False
    else:
        return True
def withPlayer():
    while not (isBoardFull(board)):
        if not(isWinner(board, p2)):
            player1Move()
            printBoard(board)
        else:
            print(p2+ " won this time! ")
            break
        if not(isWinner(board, p1)):
            if isBoardFull(board):
                print("Tie game")
            player2Move()
            printBoard(board)
        else:
            print(p1 + " won this time! ")
            break

def withAI():
    while not (isBoardFull(board)):
        if not(isWinner(board, p2)):
            player1Move()
            printBoard(board)
        else:
            print(p2+ " won this time! ")
            break
        if not(isWinner(board, p1)):
            if isBoardFull(board):
                print("Tie game")
            aiMove()
            printBoard(board)
        else:
            print(p1 + " won this time! ")
            break




print("welcome tic tac toe")
printBoard(board)

print("Choose the mode of game ")
print("1. 2 player")
print("2. with AI")
x = int(input())
if x==1:
    i = input("Choose (x/o):")
    choose(i)
    withPlayer()
elif x==2:
    i = input("Choose (x/o):")
    choose(i)
    withAI()
else:
    print("Choose the mode of game ")
    print("1. 2 player")
    print("2. with AI")
    x = int(input())




'''
board = [' ' for X in range(10)]

def printBoard(board):
    print(" " + board[1] +"| " + board[2] +"| " + board[3])
    print("---------")
    print(" " + board[4] + "| " + board[5] + "| " + board[6])
    print("---------")
    print(" " + board[7] + "| " + board[9] + "| " + board[3])

printBoard(board)

#board is full
def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

#check winner
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)
#Note that all this code falls on line.
#Do not go to the next line.
#"bo" stands for the board.
#"le" stands for the letter or symbol we're checking.

#Insert letter
def insertLetter(letter, pos):
    board[pos] = letter

#Check free position
def spaceIsFree(pos):
    return board[pos] == " "

#Play move
def playMove():
    run = True
    while run:
        move = int(input("Please select position for 'X'(1-9)"))
        try:
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter("X", move)
                else:
                    print("Sorry this space is occupied")
            else:
                print("Please type the number within the range")
        except:
            print("please type a number.")

#Computer move
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    # The above line justs checks for empty slots in the board
    move = 0
    for let in ['o', 'x']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
                # This checks if one of the players has a wining move
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
            # This checks for open corners
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move

    #This checks for open middle slot.
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move


#select random
def selectRandom(li):
#li is the list of open spots.
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def main():
    print("welcome tic tac toe")
    printBoard(board)
#prints out the board
    while not(isBoardFull(board)):
#This runs when the board isn't full
        if not(isWinner(board, "o")):
            playMove()
            printBoard(board)
        else:
            print("Sorry, O's won this time! ")
            break
#This checks if the computer has won
        if not(isWinner(board, "x")):
            move  = compMove()
#The computer checks if it can make a move
            if move == 0:
                print("Tie game")
            else:
                insertLetter("o", move)
                print("Comp placed an 'o' in position", move, ":")
                printBoard(board)
        else:
            print("X's won this time! Good job")
            break
#This checks if the user has won
#if the board is the board is full then it is tie
    if isBoardFull(board):
        print("Tie game")
'''


