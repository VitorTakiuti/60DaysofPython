def transpose_matrix(matrix):
    """
    Generate a matrix 3x3
    Substitute Horizontal Columns with Vertical ones
    [1, 2, 3]
    [1, 2, 3]
    [1, 2, 3]
    .
    .
    [1, 1, 1]
    [2, 2, 2]
    [3, 3, 3]
    
    Arg: Matrix 
    return: transpose matrix
    raises: ValueError: if matrix is not 3x3
    """
    
    if len(matrix) != 3 or not all(len(line) == 3 for line in matrix) :
        raise ValueError("Matrix isn't 3x3")
    
    transpose = [[matrix[j][i] for j in range(3)] for i in range(3)]
    
    return transpose

#Explaining the transpose function more deeply    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = []

for i in range(3):
    new_line = []
    
    for j in range(3):
        new_line.append(matrix[j][i])
        
    #print(new_line)
    transpose.append(new_line)
    
for line in transpose_matrix(matrix):
    print(line)
    
#print(transpose_matrix(matrix))
    
    