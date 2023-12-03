def gauss_elimination_pivoting(A, b):
    n = len(A)

    for i in range(n):
        pivot = abs(A[i][i])
        pivot_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > pivot:
                pivot = abs(A[j][i])
                pivot_row = j

        if pivot_row != i:
            A[i], A[pivot_row] = A[pivot_row], A[i]
            b[i], b[pivot_row] = b[pivot_row], b[i]

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    return x
