import pprint

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
        
    for num in range(1,10):
        if valid(board,num,(row,col)):
            board[row][col]=num
            
            if Solve(board):
                return True
            board[row][col]=0
    return False

def valid (board,num,pos):
    #column
    for a in range(len(board)):
        if board[a][pos[1]] == num and pos[0]!= a:
            return False
    #row
    for b in range(len(board)):
        if board[pos[0]][b] == num and pos[1]!= b:
            return False
    #check the local box
    x = pos[1] // 3
    y = pos[0] // 3
    for i in range(y*3, y*3 + 3):
        for j in range(x * 3, x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

#see if board is empty. if not return first empty coordinate    
def empty(board):
    for a in range(len(board)):
        for b in range(len(board)):
            if board[a][b] == 0 : 
                return (a,b)
    return None        

def print_board(board):
    for a in range(len(board)):
        if a%3 == 0 and a!=0:
            print ("- - - - - - - - - - - - - ")
        for b in range(len(board[0])):
            if b % 3 == 0 and b != 0:
                print(" | ", end="")

            if b == 8:
                print(board[a][b])
            else:
                print(str(board[a][b]) + " ", end="")
                
print("The original board was:")
print_board(board1)
Solve(board1)

print(" ")
print("now the solved board is:")
print_board(board1)