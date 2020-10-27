matrix = [
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

size = len(matrix)

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
    return None
                

def validity(num, pos):
    # x, y = pos
    
    # iterate each row
    for i in range(size):               # if pos is the position just inserted, ignore the pos
        if matrix[pos[0]][i] == num and pos[1] != i:
            return False
    
    # iterate each col
    for i in range(size):
        if matrix[i][pos[1]] == num and pos[0] != i:
            return False
            
    # check each box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if matrix[i][j] == num and (i, j) != pos:
                return False
    
    return True
    

def solve():
    find = find_empty(matrix)
    if not find: 
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if validity(i, (row, col)):
            matrix[row][col] = i
            if solve():
                return True
                
            matrix[row][col] = 0
    return False
    
    
print_matrix(matrix)
solve()
print("-------------")
print("")
print_matrix(matrix)