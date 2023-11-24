import sys

apart = [[0 for _ in range(15)] for _ in range(15)]
sum = [[0 for _ in range(15)] for _ in range(15)]

for j in range(1, 15):
    apart[0][j] = j
    sum[0][j] += sum[0][j - 1] + j

for i in range(1, 15):
    for j in range(1, 15):
        apart[i][j] = sum[i - 1][j]
        sum[i][j] = sum[i][j - 1] + apart[i][j]

for _ in range(int(input())):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    print(apart[k][n])