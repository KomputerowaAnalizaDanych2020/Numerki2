
def matrix_create(matrix_given):
    x_dim=len(matrix_given)
    y_dim=len(matrix_given[0])
    matrix_of_zeros = [[0 for col in range(y_dim)] for row in range(x_dim)]
    """row=[]
    for i in range(y_dim):
        row.append(0)
    matrix_of_zeros=[]
    for i in range(x_dim):
        matrix_of_zeros.append(row)
    """
    return matrix_of_zeros
def equ_and_res(given_matrix):
    results=[]
    equations=[]
    for row in given_matrix:
        results.append(row.pop())
        equations.append(row)
    return equations, results
def add_matrixes(A,B):
    result_matrix=matrix_create(A)
    for row in range (len(A)):
        for col in range (len(A[0])):
            result_matrix[row][col]=A[row][col]+B[row][col]
    return result_matrix
def matrix_minus_one_pow(matrix):
    for row in range (len(matrix)):
        for col in range (len(matrix[0])):
            if matrix[row][col]!=0:
                matrix[row][col]=1/matrix[row][col]
    return matrix
def MDivide(matrix_to_split):
    #print(matrix_to_split)
    L = matrix_create(matrix_to_split)
    D = matrix_create(matrix_to_split)
    U = matrix_create(matrix_to_split)
    print(matrix_to_split)
    for row in range(len(matrix_to_split)):

        for col in range(len(matrix_to_split[0])):
            if row == col:
                D[row][col] = matrix_to_split[row][col]
            elif row > col:
                L[row][col] = matrix_to_split[row][col]
            elif col > row:
                #print(row)
                #print(col)
                #print(matrix_to_split[row][col])
                U[row][col] = matrix_to_split[row][col]
                #print(U)
    #print(L)
    #print(D)
    #print(U)
    return L,D,U
def multiply_matrixes(A,B):
    multiplied = [[0 for x in range(len(A[0]))] for y in range(len(B))]

    # explicit for loops
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                # resulted matrix
                multiplied[i][j] += A[i][k] * B[k][j]
    return multiplied
with open('macierz.txt', 'r') as f:
    matrix = [[int(num) for num in line.split(',')] for line in f]
#print(matrix)
equ, res = equ_and_res(matrix)
lmat , dmat, umat = MDivide(equ)

added=add_matrixes(lmat,umat)
matrix_minus_one_pow(dmat)
result=multiply_matrixes(dmat,added)

#print(equ)
#print(res)
#print(matrix_create(equ))
print(lmat)
print(dmat)
print(umat)
print(added)
print(result)




