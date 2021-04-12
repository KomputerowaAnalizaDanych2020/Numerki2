
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
    L = matrix_create(matrix_to_split)
    D = matrix_create(matrix_to_split)
    U = matrix_create(matrix_to_split)
    for row in range(len(matrix_to_split)):
        for col in range(len(matrix_to_split[0])):
            if row == col:
                D[row][col] = matrix_to_split[row][col]
            elif row > col:
                L[row][col] = matrix_to_split[row][col]
            elif col > row:
                U[row][col] = matrix_to_split[row][col]
    return L,D,U
def multiply_matrixes(A,B):
    multiplied = [[0 for x in range(len(A[0]))] for y in range(len(B))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                multiplied[i][j] -= A[i][k] * B[k][j]
    return multiplied
def matrix_vector(A,B):
    vector=[0]*len(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            vector[i]+=B[i]*A[i][j]
    return vector



def get_result(M,res):
    arguments=[0]*len(M)
    for i in range (len(M)):
        x=qmat[i]
        for col in range (len(M[i])):
            if M[i][col] != 0:
                x+=M[i][col]*arguments_list[col]
        arguments[i]=x
    return arguments

def check_dominant(matrix_to_check):
    columns=[0]*len(matrix_to_check[0])
    rows = [0] * len(matrix_to_check)

    for i in range(len(matrix_to_check)):
        for j in range (len(matrix_to_check[0])):
            if (i!=j):
                rows[i]+=matrix_to_check[i][j]
                columns[j]+=matrix_to_check[i][j]
    for i in range(len(matrix_to_check)):
        if (matrix_to_check[i][i]<columns[i]):
            return False
        if (matrix_to_check[i][i] < rows[i]):
            return False
    return True

print("Rozwiazywanie ukladu N rownan liniowych z N niewiadomymi za pomoca metody iteracyjnej Jacobiego")
# Podanie funkcji jako odczyt z pliku
print("Wybierz kryterium zatrzymania:")
print("1. Spelnienie warunku nalozonego na dokladnosc")
print("2. Osiagniecie zadanej liczby iteracji")
stopChoice = input()
if stopChoice == 1:
    epsilon = input("Podaj epsilon: ")
if stopChoice == 2:
    counter = input("Podaj liczbe iteracji: ")
with open('macierz.txt', 'r') as f:
    matrix = [[int(num) for num in line.split(',')] for line in f]
if(check_dominant(matrix)):
    arguments_list = [0] * len(matrix)
    equ, res = equ_and_res(matrix)
    lmat, dmat, umat = MDivide(equ)
    added = add_matrixes(lmat, umat)
    matrix_minus_one_pow(dmat)
    resultmat = multiply_matrixes(dmat, added)
    qmat = matrix_vector(dmat, res)
    for i in range(24):
        arguments_list = get_result(resultmat, res)
    print(arguments_list)
else:
    print("Macierz nie jest macierza dominującą przekątniowo")





