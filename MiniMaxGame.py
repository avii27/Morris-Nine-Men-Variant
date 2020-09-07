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

def miniMaxGame(d, gBoard, playerFlag):
    op = MorrisBoard.outputClass()
    ip = MorrisBoard.outputClass()
    board = list()

    if(d == 0):
        numWhite = 0
        numBlack = 0
        endCount = 0

        for i in range(0, len(gBoard)):
            if(gBoard[i] == 'W'):
                numWhite = numWhite + 1
            elif(gBoard[i] == 'B'):
                numBlack = numBlack + 1
                
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

        return op
    
    if(playerFlag == 1):
        board = MorrisBoard.generateMovesMidgameEndgame(gBoard)
        op.value = vMin
    else:
        board = MorrisBoard.generateMovesMidgameEndgameBlack(gBoard)
        op.value = vMax
        
    for i in board:
        if(playerFlag == 1):
            ip = miniMaxGame(d - 1, i, 0)
            if(ip.value > op.value):
                op.value = ip.value
                op.boardState = i
            op.count = op.count + ip.count
            
        else:
            ip = miniMaxGame(d - 1, i, 1)
            if(ip.value < op.value):
                op.value = ip.value
                op.boardState = i
            op.count = op.count + ip.count

    return op

bState = getState()  
output = miniMaxGame(depth, bState, 1)
print("Board Position: ", ''.join(output.boardState))
print("Position evaluated by Static Estimation:", output.count)
print("MINIMAX Estimate:", output.value)
writeState(output.boardState)