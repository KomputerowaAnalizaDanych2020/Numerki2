#stwórz macierz zerową, odpowiadającej wielkości macierzy zadanej
def matrix_create(matrix_given):
    x_dim = len(matrix_given)
    y_dim = len(matrix_given[0])
    matrix_of_zeros = [[0 for col in range(y_dim)] for row in range(x_dim)]
    return matrix_of_zeros


#rozdziel macierz równań i wyników na 2 odzielne
def equ_and_res(given_matrix):
    results = []
    equations = []
    for row in given_matrix:
        results.append(row.pop())
        equations.append(row)
    return equations, results


#dodaje 2 macierze
def add_matrixes(A, B):
    result_matrix = matrix_create(A)
    for row in range(len(A)):
        for col in range(len(A[0])):
            result_matrix[row][col] = A[row][col]+B[row][col]
    return result_matrix


#podnosi macierz do potęgi ^-1
def matrix_minus_one_pow(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != 0:
                matrix[row][col] = 1/matrix[row][col]
    return matrix


#zwraca macierz dolna macierz trojkatna, gorna macierz trójkątną oraz macierz diagonalna z zadanej macierzy
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
    return L, D, U


#mnoży 2 macierze
def multiply_matrixes(A,B):
    multiplied = [[0 for x in range(len(A[0]))] for y in range(len(B))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                multiplied[i][j] -= A[i][k] * B[k][j]
    return multiplied


#mnoży wektor razy macierz
def matrix_vector(A, B):
    vector=[0]*len(A)
    for i in range(len(A)):
        for j in range(len(A[0])):
            vector[i] += B[i]*A[i][j]
    return vector


#algorytm metody Jakobiego
def get_result(M,res):
    arguments = [0]*len(M)      #startowy wektor 0
    for i in range(len(M)):
        x = qmat[i]
        for col in range(len(M[i])):
            if M[i][col] != 0:
                x += M[i][col]*arguments_list[col]
        arguments[i] = x
    return arguments


#sprawdzenie czy zadana macierz jest silnie diagonalna
def check_dominant(matrix_to_check):
    columns = [0]*len(matrix_to_check[0])
    rows = [0] * len(matrix_to_check)

    for i in range(len(matrix_to_check)):
        for j in range (len(matrix_to_check[0])):
            if i != j:
                rows[i] += matrix_to_check[i][j]
                columns[j] += matrix_to_check[i][j]
    for i in range(len(matrix_to_check)):
        if matrix_to_check[i][i]<columns[i]:
            return False
        if matrix_to_check[i][i] < rows[i]:
            return False
    return True


#funkcja licząca bląd bezwzgledny
def delta(arguments,expected,equations):
    errors = 0
    for row in range(len(equations)):
        actual = 0
        for column in range(len(equations)):
            actual += equations[row][column]*arguments[column]
        errors += abs(abs(actual)-abs(expected[row]))
    return errors

print("Rozwiazywanie ukladu N rownan liniowych z N niewiadomymi za pomoca metody iteracyjnej Jacobiego")
print("Wybierz kryterium zatrzymania:")
print("1. Spelnienie warunku nalozonego na dokladnosc")
print("2. Osiagniecie zadanej liczby iteracji")
stopChoice = input()
counter = 10000000
epsilon=0.0000000000000001
if stopChoice == "1":
    epsilon = float(input("Podaj epsilon: "))
if stopChoice == "2":
    counter = int(input("Podaj liczbe iteracji: "))
with open('macierz.txt', 'r') as f:
    matrix = [[float(num) for num in line.split(',')] for line in f]
equ, res = equ_and_res(matrix)
if check_dominant(equ):
    arguments_list = [0] * len(matrix)              #początkowe przyblizenie
    lmat, dmat, umat = MDivide(equ)                 # L D U
    added = add_matrixes(lmat, umat)
    matrix_minus_one_pow(dmat)
    resultmat = multiply_matrixes(dmat, added)
    qmat = matrix_vector(dmat, res)
    while counter > 0 and epsilon < delta(arguments_list, res, equ):
        arguments_list = get_result(resultmat, res)
        counter -= 1
    print("Otrzymane przybliżenia x: ")
    print(arguments_list)
else:
    print("Macierz nie jest macierza dominującą przekątniowo")





