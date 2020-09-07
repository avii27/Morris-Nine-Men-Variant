import sys
import MorrisBoard

vMax = sys.maxsize
vMin = -sys.maxsize
depth = int(sys.argv[3])
bState = list()

def getState():
    tempB = open(sys.argv[1], "r")
    board = list()
    
    for line in tempB:
        for ch in line:
            board.append(ch)
    tempB.close()

    return board

def writeState(outBoardState):
    tempB = open(sys.argv[2], "w")
    
    for i in outBoardState:
        tempB.write(i)
    tempB.close()

def SEO(state):
    numWhite = 0
    numBlack = 0

    for i in range(0, len(state)):
        if(state[i] == 'W'):
            numWhite = numWhite + 1
        
        elif(state[i] == 'B'):
            numBlack = numBlack + 1

    return numWhite - numBlack

def ABGame(d, gBoard, alpha, beta, playerFlag):
    op = MorrisBoard.outputClass()
    ip = MorrisBoard.outputClass()
    
    if(d == 0):
        numWhite = 0
        numBlack = 0
        endCount = 0

        for i in range(0, len(gBoard)):
            if(gBoard[i] == 'W'):
                numWhite = numWhite+1
            if(gBoard[i] == 'B'):
                numBlack = numBlack+1
        endCount = numWhite - numBlack
        l = MorrisBoard.generateMovesMidgameEndgameBlack(gBoard)
        lSize = len(l)
        if(numBlack <= 2):
            op.value = 10000
        elif(numWhite <= 2):
            op.value = -10000
        elif(lSize == 0):
            op.value = 10000
        else:
            op.value = 1000 * (endCount) - lSize
        op.count = op.count + 1
        op.boardState = gBoard

        return op
    
    moveL = list()
    if(playerFlag==1):    
        moveL = MorrisBoard.generateMovesMidgameEndgame(gBoard)   
    else:
        moveL = MorrisBoard.generateMovesMidgameEndgameBlack(gBoard)
            
    for i in moveL:
        if(playerFlag == 1):
            ip = ABGame(d - 1, i, alpha, beta, 0)
            if(ip.value > alpha):
                alpha = ip.value
                op.boardState = i
            op.count = op.count + ip.count
        else:
            ip = ABGame(d - 1, i, alpha, beta, 1)
            if(ip.value < beta):
                beta = ip.value
                op.boardState = i
            op.count = op.count + ip.count
        if(alpha >= beta):
            break
        
    if (playerFlag == 1):
        op.value = alpha
    else:
        op.value = beta
    return op

bState = getState()  
output = ABGame(depth, bState, vMin, vMax, 1)
print("Board Position: ", ''.join(output.boardState))
print("Position evaluated by Static Estimation: ", output.count)
print("MINIMAX Estimate: ", output.value)
writeState(output.boardState)