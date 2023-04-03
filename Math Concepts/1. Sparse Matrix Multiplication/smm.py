def sparse_matrix_multiplication(matrix_a, matrix_b):
    # matrix a is M x N
    # matrix b is P x Q
    M = len(matrix_a)
    N = len(matrix_a[0])

    P = len(matrix_b)
    Q = len(matrix_b[0])

    # matrix multiplication check
    if N != P:
        return [[]]

    # define matrix c as M x Q
    matrix_c = [[0] * Q for _ in range(M)]

    sparse_a = nonzero_cells(matrix_a)
    sparse_b = nonzero_cells(matrix_b)

    for i, k in sparse_a.keys():
        for j in range(Q):
            if (k, j) in sparse_b.keys():
                matrix_c[i][j] += sparse_a[(i, k)] * sparse_b[(k, j)]
    return matrix_c

def nonzero_cells(matrix):
    # dictionary to store all non zero values
    sparse_dict = {}
    
    # loop through matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                sparse_dict[(i, j)] = matrix[i][j]
    
    return sparse_dict

if __name__ == "__main__":

    matrix_a = [
        [0, 2, 0],
        [0, -3, 5]
    ]

    matrix_b = [
    [0, 10, 0],
    [0, 0, 0],
    [0, 0, 4]
    ]

    print(sparse_matrix_multiplication(matrix_a, matrix_b))