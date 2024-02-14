# 걸린 시간 : 20분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

from itertools import permutations
from collections import deque

def ccw(a, b, c):
    return a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

answer = 40320
root_2 = 2 ** 0.5
for A in permutations(map(int, input().split()), 8):
    pairs = deque([(0, A[0]), (A[1] / root_2, A[1] / root_2), (A[2], 0), (A[3] / root_2, -A[3] / root_2),
                   (0, -A[4]), (-A[5] / root_2, -A[5] / root_2), (-A[6], 0), (-A[7] / root_2, A[7] / root_2)])

    for _ in range(8):
        if ccw(pairs[0], pairs[1], pairs[2]) > 0:
            answer -= 1
            break
        pairs.rotate(1)

print(answer)