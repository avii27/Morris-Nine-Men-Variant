from copy import deepcopy

class outputClass(object):
    count = 0
    value = 0
    boardState = list()
    
    def __init__(self,value=0,count=0,boardState=list()):
        self.count = count
        self.value = value
        self.boardState = boardState
    
def flipBoard(boardtoflip):
    b = list(range(0,23))
    for i in range(0,len(boardtoflip)):
        if(boardtoflip[i]=='B'):
            b[i]='W'
        elif(boardtoflip[i]=='W'):
            b[i]='B'
        else:
            b[i]='x'
    return b
    
def generateMoveOpening(boardPostion):
    listOfBoardPosition = list()
    listOfBoardPosition = generateAdd(boardPostion)
    return listOfBoardPosition

def generateMoveOpeningBlack(b):
    tempb = flipBoard(b)
    blackMoves = list()
    blackMoves = generateAdd(tempb)
    moves = list()
    
    for each in range(0,len(blackMoves)):
        b = blackMoves[each]
        moves.insert(each,flipBoard(b))
    return moves 

def closeMill(position,b):
    C = b[position]
    if(C=='x'):
        return False
    else:
        return checkMills(position,b,C)

def checkMills(position,b,C):
    if(C=='x'):
        return False
    
    if(position==0):
        if((b[1]==C and b[2]==C) or (b[3]==C and b[6]==C) or (b[8]==C and b[20]==C)):
            return True
        return False
    
    elif(position==1):
        if(b[0]==C and b[2]==C):
            return True
        return False
    
    elif(position==2):
        if((b[0]==C and b[1]==C) or (b[5]==C and b[7]==C) or (b[13]==C and b[22]==C)):
            return True
        return False
    
    elif(position==3):
        if((b[0]==C and b[6]==C) or (b[4]==C and b[5]==C) or (b[9]==C and b[17]==C)):
            return True
        return False
    
    elif(position==4):
        if(b[3]==C and b[5]==C):
            return True
        return False

    elif(position==5):
        if((b[3]==C and b[4]==C) or (b[2]==C and b[7]==C) or (b[12]==C and b[19]==C)):
            return True
        return False    
    
    elif(position==6):
        if((b[0]==C and b[3]==C) or (b[10]==C and b[14]==C)):
            return True
        return False 
    
    elif(position==7):
        if((b[2]==C and b[5]==C) or (b[11]==C and b[16]==C)):
            return True
        return False
    
    elif(position==8):
        if((b[0]==C and b[20]==C) or (b[9]==C and b[10]==C)):
            return True
        return False
    
    elif(position==9):
        if((b[8]==C and b[10]==C) or (b[3]==C and b[17]==C)):
            return True
        return False

    elif(position==10):
        if((b[8]==C and b[9]==C) or (b[6]==C and b[14]==C)):
            return True
        return False 
    
    elif(position==11):
        if((b[7]==C and b[16]==C) or (b[12]==C and b[13]==C)):
            return True
        return False
    
    elif(position==12):
        if((b[11]==C and b[13]==C) or (b[5]==C and b[19]==C)):
            return True
        return False
    
    elif(position==13):
        if((b[11]==C and b[12]==C) or (b[2]==C and b[22]==C)):
            return True
        return False    
    
    elif(position==14):
        if((b[17]==C and b[20]==C) or (b[15]==C and b[16]==C) or (b[6]==C and b[10]==C)):
            return True
        return False 
    
    elif(position==15):
        if((b[14]==C and b[16]==C) or (b[18]==C and b[21]==C)):
            return True
        return False
    
    elif(position==16):
        if((b[14]==C and b[15]==C) or (b[19]==C and b[22]==C) or (b[7]==C and b[11]==C)):
            return True
        return False

    elif(position==17):
        if((b[3]==C and b[9]==C) or (b[14]==C and b[20]==C) or (b[18]==C and b[19]==C)):
            return True
        return False

    elif(position==18):
        if((b[17]==C and b[19]==C) or (b[15]==C and b[21]==C)):
            return True
        return False
    
    elif(position==19):
        if((b[17]==C and b[18]==C) or (b[16]==C and b[22]==C) or (b[5]==C and b[12]==C)):
            return True
        return False    
    
    elif(position==20):
        if((b[0]==C and b[8]==C) or (b[14]==C and b[17]==C) or (b[21]==C and b[22]==C)):
            return True
        return False
    
    elif(position==21):
        if((b[20]==C and b[22]==C) or (b[15]==C and b[18]==C)):
            return True
        return False
    
    elif(position==22):
        if((b[2]==C and b[13]==C) or (b[16]==C and b[19]==C) or (b[20]==C and b[21]==C)):
            return True
        return False
    else:
        return False
    
def generateRemove(boardPos,L):
    for i in range(0,len(boardPos)):
        if boardPos[i]=='B':
            if(closeMill(i,boardPos)==False):
                b_updated = deepcopy(boardPos)   
                b_updated[i]='x'
                L.append(b_updated)

    return L

def generateAdd(boardPosition):
    L = list()
    for i in range(0,len(boardPosition)):
        if(boardPosition[i]=='x'):
            b = deepcopy(boardPosition)
            b[i]='W'
            if (closeMill(i,b)):
                L = generateRemove(b,L)
            else:
                L.append(b)

    return L

def neighbors(position):
    neighbourL = list()
    
    if(position==0):
        neighbourL.append(1)
        neighbourL.append(3)
        neighbourL.append(8)
        
    elif(position==1):
        neighbourL.append(0)
        neighbourL.append(2)
        neighbourL.append(4)
        
    elif(position==2):
        neighbourL.append(1)
        neighbourL.append(5)
        neighbourL.append(13)
        
    elif(position==3):
        neighbourL.append(0)
        neighbourL.append(4)
        neighbourL.append(6)
        neighbourL.append(9)
        
    elif(position==4):
        neighbourL.append(1)
        neighbourL.append(3)
        neighbourL.append(5)
        
    elif(position==5):
        neighbourL.append(2)
        neighbourL.append(4)
        neighbourL.append(7)
        neighbourL.append(12)

    elif(position==6):
        neighbourL.append(3)
        neighbourL.append(7)
        neighbourL.append(10)
    
    elif(position==7):
        neighbourL.append(5)
        neighbourL.append(6)
        neighbourL.append(11)
    
    elif(position==8):
        neighbourL.append(0)
        neighbourL.append(9)
        neighbourL.append(20)
        
    elif(position==9):
        neighbourL.append(3)
        neighbourL.append(8)
        neighbourL.append(10)
        neighbourL.append(17)
        
    elif(position==10):
        neighbourL.append(6)
        neighbourL.append(9)
        neighbourL.append(14)
        
    elif(position==11):
        neighbourL.append(7)
        neighbourL.append(12)
        neighbourL.append(16)
        
    elif(position==12):
        neighbourL.append(5)
        neighbourL.append(11)
        neighbourL.append(13)
        neighbourL.append(19)
       
    elif(position==13):
        neighbourL.append(2)
        neighbourL.append(12)
        neighbourL.append(22)    
     
    elif(position==14):
        neighbourL.append(10)
        neighbourL.append(15)
        neighbourL.append(17)
        
    elif(position==15):
        neighbourL.append(14)
        neighbourL.append(16)
        neighbourL.append(18)
        
    elif(position==16):
        neighbourL.append(11)
        neighbourL.append(15)
        neighbourL.append(19)
        
    elif(position==17):
        neighbourL.append(9)
        neighbourL.append(14)
        neighbourL.append(18)
        neighbourL.append(20)
    
     
    elif(position==18):
        neighbourL.append(15)
        neighbourL.append(17)
        neighbourL.append(19)
        neighbourL.append(21)
        
    elif(position==19):
        neighbourL.append(12)
        neighbourL.append(16)
        neighbourL.append(18)
        neighbourL.append(22)
        
    elif(position==20):
        neighbourL.append(8)
        neighbourL.append(17)
        neighbourL.append(21)
        
    elif(position==21):
        neighbourL.append(18)
        neighbourL.append(20)
        neighbourL.append(22)
        
    elif(position==22):
        neighbourL.append(13)
        neighbourL.append(19)
        neighbourL.append(21)
    else:
        return neighbourL
        
    return neighbourL

def generateMove(boardPosition):
    L = list()

    for i in range(0,len(boardPosition)):
        if(boardPosition[i]=='W'):
            n = neighbors(i)
            for j in n:
                if(boardPosition[j]=='x'):
                    b = deepcopy(boardPosition)
                    b[i]='x'
                    b[j]='W'
                    if(closeMill(j,b)):
                        L = generateRemove(b,L)
                    else:
                        L.append(b)
    return L
                     

def generateMovesMidgameEndgame(boardPosition):
    numWhite = 0
    l = list()
    for position in range(0,len(boardPosition)):
        if(boardPosition[position]=='W'):
            numWhite = numWhite+1
    
    if(numWhite==3):
        l = generateHopping(boardPosition)
    else:
        l = generateMove(boardPosition)
    return l

def generateMovesMidgameEndgameBlack(boardPosition):
    temp = flipBoard(boardPosition)
    l = list()
    L = generateMovesMidgameEndgame(temp)
    for i in range(0,len(L)):
        b = L[i]
        l.insert(i,flipBoard(b))
    return l
    
def generateHopping(boardPosition):
    L = list()
    for alpha in range(0,len(boardPosition)):
        if(boardPosition[alpha]=='W'):
            for beta in range(0,len(boardPosition)):
                if (boardPosition[beta]=='x'):
                    b = deepcopy(boardPosition)
                    b[alpha]='x'
                    b[beta]='W'
                    if(closeMill(beta,b)):
                        L = generateRemove(b,L)
                    else:
                        L.append(b)
    return L