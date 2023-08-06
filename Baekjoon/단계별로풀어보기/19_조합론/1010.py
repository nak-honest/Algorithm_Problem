T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    arr = [[1 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(1, n + 1):
            if j != i:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

    print(arr[m][n])