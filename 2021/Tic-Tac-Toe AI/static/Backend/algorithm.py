import random
import math


# coinToss determines who goes first
def coinToss(Value):
    randToss = random.randint(0, 1)

    if Value == randToss:
        return True
    else:
        return False


# Check to see if there is a win condition satisfied
def checkWin(board):
    # 1 = AI
    # -1 = Player
    # 0 = draw
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
    return bestMove


# miniMax Algorithm
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
