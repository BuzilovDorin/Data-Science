import math
import random

startBoard = ["none", "none", "none", "none",
              "none", "none", "none", "none", "none"]


def printboard(board):
    print(" ")
    print(board[0], " | ", board[1], " | ", board[2])
    print("- - - - - - - - - - - -")
    print(board[3], " | ", board[4], " | ", board[5])
    print("- - - - - - - - - - - -")
    print(board[6], " | ", board[7], " | ", board[8])
    print(" ")


def checkWin(board):
    row = 0
    for i in range(3):
        # Checking Columns
        if board[i] == board[i + 3] and board[i + 3] == board[i + 6]:
            if board[i] == "x":
                return -1
            if board[i] == "o":
                return 1
        # Checking Rows
        if board[row] == board[row + 1] and board[row + 1] == board[row + 2]:
            if board[row] == "x":
                return -1
            if board[row] == "o":
                return 1
        row += 3
    # Checking Diagonal
    if board[0] == board[4] and board[4] == board[8]:
        if board[0] == "x":
            return -1
        if board[0] == "o":
            return 1
    if board[2] == board[4] and board[4] == board[6]:
        if board[2] == "x":
            return -1
        if board[2] == "o":
            return 1
    # Checking Draw
    if "none" not in board:
        return 0
    else:
        return None
    # # 1 = AI
    # # -1 = Player
    # # 0 = draw


def AiTurn(board):
    bestScore = -math.inf
    bestMove = None
    for i in range(9):
        if board[i] == "none":
            board[i] = "o"
            score = miniMax(board, -2, 2, False)
            board[i] = "none"
            if score > bestScore:
                bestScore = score
                bestMove = i
    board[bestMove] = "o"

    printboard(board)
    # Check if there is terminal State
    win = checkWin(board)
    if win != None:
        if win == 1:
            print("AI has won!!!")
            exit()
        elif win == -1:
            print("Player has won!!")
            exit()
        else:
            print("~ It's a Draw ~")
            exit()

    PlayerTurn(board)


# Alpha & Beta Pruning is applied to reduce number of computations the computer needs to perform
# Alpha is best option already explored for Max Player
# Beta is best option already explored for Min Player
def miniMax(board, alpha, beta, isMax):
    result = checkWin(board)
    if result != None:
        return result

    if isMax:
        bestScore = -math.inf
        for i in range(9):
            if board[i] == "none":
                board[i] = "o"
                score = miniMax(board, alpha, beta, False)
                board[i] = "none"
                bestScore = max(score, bestScore)

                if bestScore >= beta:
                    return(bestScore)

                if bestScore > alpha:
                    alpha = bestScore
        return bestScore
    else:
        bestScore = math.inf
        for i in range(9):
            if board[i] == "none":
                board[i] = "x"
                score = miniMax(board, alpha, beta, True)
                board[i] = "none"
                bestScore = min(score, bestScore)

                if bestScore <= alpha:
                    return(bestScore)

                if bestScore < beta:
                    beta = bestScore
        return bestScore


def PlayerTurn(board):
    print(" ")
    print("What's your next move?:")
    posX = int(input("Position 1-9:"))
    if posX not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("Thats not a valid position!!")
        PlayerTurn(board)
    if board[posX-1] in ["x", "o"]:
        print("That position is occupied!!")
        PlayerTurn(board)

    board[posX-1] = "x"

    printboard(board)
    # Check if there is terminal State
    win = checkWin(board)
    if win != None:
        if win == 1:
            print("AI has won!!!")
            exit()
        elif win == -1:
            print("Player has won!!")
            exit()
        else:
            print("~ It's a Draw ~")
            exit()

    AiTurn(board)


def coinToss():
    print(" ")
    print("~ Calls heads or tails to see who goes first ~")
    choice = int(input("Choose Heads[1] or Tails[2]: "))
    if choice not in [1, 2]:
        coinToss()
    return choice


# Script Start here with coinflip
coinflip = random.randint(1, 2)
c = coinToss()
printboard(startBoard)
if c == coinflip:
    PlayerTurn(startBoard)
else:
    AiTurn(startBoard)
