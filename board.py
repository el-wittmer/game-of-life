#board idea
living = [(0,0), (3,0), (2,1)]
height = 3
width = 4
board = list()
row = list()

def createBlankBoard(width, height):
    board = list()
    i = 0
    while i < height:
        row = list()
        j = 0
        while j < width:
            position = False
            row.append(position)   # fill each position in the row with True
            j = j + 1 
        board.append(row)
        i = i + 1
    return board
     
def updateBoard(board, living):
    # loop through the living list getting the x,y and storing true in board
    i = 0
    new_board = list()
    while (i < len(living)):
        xy = living[i]
        row = board[xy[1]]
        row[xy[0]] = True
        board[xy[1]] = row
        i = i + 1
    return board
    
def printBoard(board):
    i = 0
    while i < len(board):
        row = board[i]
        j = 0
        while j < len(row):
            if row[j] == True:
                print ("X", end=""),
            else:
                print("O", end=""),
            j = j + 1
        print("")
        i = i + 1      
        
b = list()
print("Printing blank board")
b = createBlankBoard(width, height)
printBoard(b)
print("Printing living board")
b = updateBoard(b, living)
printBoard(b)