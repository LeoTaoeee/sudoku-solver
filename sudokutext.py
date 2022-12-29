import pprint
import numpy

#9x9 standard sudoku board
board1 = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#main function to solve the board
def Solve (board):
    temp = empty(board)
    if not temp :
        return True
    else:
        row,col = temp
        
    for i in range(1,10)

#see if board is empty. if not return first empty coordinate    
def empty(board):
    for a in range(len(board)):
        for b in range(len(board)):
            if board[a][b] == 0 : 
                return (a,b)
    return None        