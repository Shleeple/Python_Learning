from random import randrange
def DisplayBoard(board):
    print("+-------"*3,"+",sep="")
    for row in range(3):
        print("|       "*3,"|", sep="")
        for column in range(3):
            print("|  ",board[row][column],"  ", end="")
        print("|")
        print("|       "*3,"|",sep="")
        print("+-------"*3,"+",sep="")
            
def EnterMove(board):
    move = int(input("What's your move? "))
    move -=1
    row = move//3
    column = move%3
    if board[row][column] == "o":
        print("Not a valid input, try again")
        EnterMove(board)
    elif board[row][column] == "x":
        print("Not a valid input, try again")
        EnterMove(board)
    else:
        board[row][column] = "o"
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#

def MakeListOfFreeFields(board):
    free = []
    for i in range(9):
        row = i//3
        column = i%3
        if board[row][column] == "x":
            continue
        if board[row][column] == "o":
            continue
        else:
            free.append(i)
    return free      
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#

def VictoryFor(board, sign):
    for i in range(3):
        if ((board[i][0] == "o") and (board[i][1] == "o") and (board[i][2] == "o")):
            sign = "o"
        elif ((board[i][0] == "x") and (board[i][1] == "x") and (board[i][2] == "x")):
            sign = "x"
        elif ((board[0][i] == "o") and (board[1][i] == "o") and (board[2][i] == "o")):
            sign = "o"
        elif ((board[0][i] == "x") and (board[1][i] == "x") and (board[2][i] == "x")):
            sign = "x"
        elif ((board[0][i] == "x") and (board[1][i] == "x") and (board[2][i] == "x")):
            sign = "x"
        elif ((board[0][0] == "x") and (board[1][1] == "x") and (board[2][2] == "x")):
            sign = "x"
        elif ((board[2][0] == "x") and (board[1][1] == "x") and (board[0][2] == "x")):
            sign = "x"
                   
    if sign == "o":
        return True
    elif sign == "x":
        return False
    else:
        return None
        
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#

def DrawMove(board):
    freeSlot = MakeListOfFreeFields(board)
    num = len(freeSlot)
    if num > 0:
        rand = randrange(num)
        num2 = freeSlot[rand]
        row = num2//3
        column = num2%3
        board[row][column] = "x"
    else:
        return None
#
# the function draws the computer's move and updates the board
#

board=[["1","2","3"],
       ["4","x","6"],
       ["7","8","9"]]
sign = ""
condition = MakeListOfFreeFields(board)
victory = ""
while len(condition)>0:
    DisplayBoard(board)
    EnterMove(board)
    if VictoryFor(board,sign) == True:
        victory = "o"
        break;
    DrawMove(board)
    DisplayBoard(board)
    if VictoryFor(board,sign) == False:
        victory = "x"
        break;

    
    condition = MakeListOfFreeFields(board)

if victory == "x":
    print("Sorry player, the computer wins")
elif victory == "o":
    print("HEY! DAS YOU! Congrats buddy")
else:
    print("Oof, a tie? That's unlucky")
