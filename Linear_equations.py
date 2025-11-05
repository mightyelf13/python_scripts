def elimination(A):
    n = len(A)
    for i in range(n):
        max_row = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        A[i], A[max_row] = A[max_row], A[i]
        for j in range(i+1, n):
            factor = -A[j][i] / A[i][i]
            for k in range(i, n+1):
                A[j][k] += factor * A[i][k]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


if __name__ == '__main__':
    N = int(input())
    equations = []
    for _ in range(N):
        equation = list(map(int, input().split()))
        equations.append(equation)


    solution = elimination(equations)
    for _ in solution:
        print(_)