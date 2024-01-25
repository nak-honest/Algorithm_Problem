# CCW에 대해 처음 알았다. 혼자의 힘으로 풀지 못하였다.
# 앞으로 기하 문제들을 풀때 많은 도움이 될듯하다.

import sys
from math import floor
from math import ceil


# 두 a->b 벡터와 a->c 벡터의 외적의 크기를 ccw(a, b, c)라 하자.
def ccw(a, b, c):
    return a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

N = int(input())

dots = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dots.append((x, y))

answer = 0

# 기준점 하나를 잡고(A라 하자), 반시계 or 시계방향으로 돌면서 두점(B, C라 하자)에 대해 ccw(A, B, C) 값을 모두 더한다.
# 그것이 다각형의 면접이 된다.
A = dots[0]

for i in range(1, N-1):
    B = dots[i]
    C = dots[i+1]

    answer += ccw(A, B, C)

# 파이썬의 round 함수는 0.5에 대해 다르게 동작하기 때문에 직접 구현.
answer = abs(answer) * 10 / 2

if answer - floor(answer) >= 0.5:
    answer = ceil(answer)
else:
    answer = floor(answer)

print(answer / 10)
