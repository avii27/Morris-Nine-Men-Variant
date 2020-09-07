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

def SEOImp(boardSt):
    numWhite = 0
    numBlack = 0
    mills = 0
    diff = 0
    
    for i in range(0, len(boardSt)):
        if(boardSt[i] == 'W'):
            numWhite = numWhite + 1
        
        elif(boardSt[i] == 'B'):
            numBlack = numBlack+1

    diff = numWhite - numBlack 
    
    for i in range(0, len(boardSt)):
        if(boardSt[i] == 'x'):
            if(MorrisBoard.checkMills(i, boardSt, "W") == True):
                mills = mills + 1
    
    return mills + diff

def miniMax(d, gBoard, playerFlag):
    op = MorrisBoard.outputClass()
    ip = MorrisBoard.outputClass()
    board = list()

    if(d == 0):
        finalCount = SEOImp(gBoard)
        op = MorrisBoard.outputClass(finalCount, op.count + 1, gBoard)
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