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

def miniMax(d, gBoard, playerFlag):
    op = MorrisBoard.outputClass()
    ip = MorrisBoard.outputClass()
    board = list()
    endCount = 0

    if(d == 0):
        endCount = SEO(gBoard)
        op = MorrisBoard.outputClass(endCount, op.count + 1, gBoard)

        return op
    
    if(playerFlag == 1):
        board = MorrisBoard.generateMoveOpening(gBoard)
        op.value = vMin
    else:
        board = MorrisBoard.generateMoveOpeningBlack(gBoard)
        op.value = vMax
        
    for i in board:
        if(playerFlag == 1):
            ip = miniMax(d - 1, i, 0)
            if(ip.value > op.value):
                op.value = ip.value
                op.boardState = i
            op.count = op.count + ip.count
            
        else:
            ip = miniMax(d - 1, i, 1)
            if(ip.value < op.value):
                op.value = ip.value
                op.boardState = i
            op.count = op.count + ip.count
            
    return op
        
bState = getState()  
output = miniMax(depth, bState, 1)
print("Board Position: ", ''.join(output.boardState))
print("Position evaluated by Static Estimation: ", output.count)
print("MINIMAX Estimate: ", output.value)
writeState(output.boardState)