def square_matrix_multiply(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]

    return c


print(square_matrix_multiply([[3,4], [4,5]], [[1,2], [1,2]]))