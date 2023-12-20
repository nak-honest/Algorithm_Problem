# 걸린 시간 : 40분
# 제출 횟수 : 4번
# 풀이 참조 : x
# 반례 참조 : x

import sys
import math

for _ in range(int(input())):
    M, N, x, y = map(int, sys.stdin.readline().split())
    if x == M:
        x = 0
    if y == N:
        y = 0

    lcm = math.lcm(M, N)

    larger = M
    larger_r = x
    smaller = N
    smaller_r = y

    if M < N:
        larger = N
        larger_r = y
        smaller = M
        smaller_r = x

    answer = -1
    k = larger_r

    # k가 0이라는 것은 0번째 해라는 것인데, 이는 불가능 하다. 따라서 이 if문이 없다면 틀리게 된다.
    if k == 0:
        k += larger

    while k <= lcm:
        if k % smaller == smaller_r:
            answer = k
            break
        k += larger

    print(answer)

'''
k % M = x
k % N = y

k = q * M + x
K = q' * N + y

q * M + x = q' * N + y
'''