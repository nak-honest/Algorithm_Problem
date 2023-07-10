import sys

# mat ^ exp % div 를 반환한다.
def get_pow(mat, exp, div):
    n = len(mat)

    if exp == 1:
        return mat

    half = get_pow(mat, exp//2, div)
    square_half = square_mat(half, div)

    if exp % 2 == 0:
        return square_half
    else:
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += square_half[i][k] * mat[k][j]

                result[i][j] %= div

        return result

# mat^2 % div 를 반환한다.
def square_mat(mat, div):
    n = len(mat)
    result = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat[i][k] * mat[k][j]

            result[i][j] %= div

    return result


N, B = map(int, input().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# A의 원소중 1000인 원소는 mod 1000을 취해준다.
for i in range(N):
    for j in range(N):
        if A[i][j] == 1000:
            A[i][j] = 0

answer = get_pow(A, B, 1000)

for row in answer:
    print(*row)