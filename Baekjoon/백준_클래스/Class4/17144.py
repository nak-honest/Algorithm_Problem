# 걸린 시간 : 1시간
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys
from copy import deepcopy

R, C, T = map(int, input().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
cleaner_top = -1
cleaner_bottom = -1

for i in range(R):
    if A[i][0] == -1:
        cleaner_top = i
        cleaner_bottom = i+1
        break

right = []
right.extend([(cleaner_bottom, j) for j in range(1, C-1)])
right.extend([(cleaner_top, j) for j in range(1, C-1)])

left = []
left.extend([(0, j) for j in range(1, C)])
left.extend([(R-1, j) for j in range(1, C)])

up = []
up.extend([(i, C-1) for i in range(1, cleaner_top+1)])
up.extend([(i, 0) for i in range(cleaner_bottom+2, R)])

down = []
down.extend([(i, C-1) for i in range(cleaner_bottom, R-1)])
down.extend([(i, 0) for i in range(cleaner_top-1)])

remove = [(cleaner_top-1, 0), (cleaner_bottom+1, 0)]

for _ in range(T):
    new_A = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if A[i][j] >= 5:
                spread_count = 0
                spread_quantity = A[i][j] // 5

                if i - 1 >= 0 and A[i-1][j] != -1:
                    new_A[i-1][j] += spread_quantity
                    spread_count += 1

                if j - 1 >= 0 and A[i][j-1] != -1:
                    new_A[i][j-1] += spread_quantity
                    spread_count += 1

                if i + 1 < R and A[i+1][j] != -1:
                    new_A[i+1][j] += spread_quantity
                    spread_count += 1

                if j + 1 < C and A[i][j+1] != -1:
                    new_A[i][j+1] += spread_quantity
                    spread_count += 1

                new_A[i][j] += (A[i][j] - spread_count * spread_quantity)
            else:
                new_A[i][j] += A[i][j]
    A = deepcopy(new_A)

    for i, j in remove:
        A[i][j] = 0

    for i, j in right:
        A[i][j+1] += new_A[i][j]
        A[i][j] -= new_A[i][j]

    for i, j in left:
        A[i][j-1] += new_A[i][j]
        A[i][j] -= new_A[i][j]

    for i, j in down:
        A[i+1][j] += new_A[i][j]
        A[i][j] -= new_A[i][j]

    for i, j in up:
        A[i-1][j] += new_A[i][j]
        A[i][j] -= new_A[i][j]

answer = 2
for i in range(R):
    answer += sum(A[i])

print(answer)




