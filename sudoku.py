board = [
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

size = len(board)

def print_matrix(matrix):
    for i in range(size):
        if i%3 == 0 and i != 0:
            print("---------------------")
            
        for s in range(size):
            if s%3 == 0 and s != 0:
                print("| ", end="")
                
            if s == 8:
                print(matrix[i][s])
            else:
                print(str(matrix[i][s]) + " ", end="")

# return tuple of row and col, if a cell is 0            
def find_empty(matrix):
    for i in range(size):
        for s in range(size):
            if matrix[i][s] == 0:
                return (i, s)
                

def validity(matrix, num, pos):
    # iterate each row
    for i in range(size):
        if matrix[pos[0]][i] == num and pos[1] != i:
            return False
        
    