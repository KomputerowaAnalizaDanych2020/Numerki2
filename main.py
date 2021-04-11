
def matrix_create(matrix_given):
    x_dim=len(matrix_given)
    y_dim=len(matrix_given[0])
    row=[]
    for i in range(y_dim):
        row.append(0)
    matrix_of_zeros=[]
    for i in range(x_dim):
        matrix_of_zeros.append(row)
    return matrix_of_zeros
def equ_and_res(given_matrix):
    results=[]
    equations=[]
    for row in given_matrix:
        results.append(row.pop())
        equations.append(row)
    return equations, results
def MDivide(matrix_to_split):
    L
with open('macierz.txt', 'r') as f:
    matrix = [[int(num) for num in line.split(',')] for line in f]
print(matrix)
equ, res = equ_and_res(matrix)


print(equ)
print(res)
print(matrix_create(equ))


