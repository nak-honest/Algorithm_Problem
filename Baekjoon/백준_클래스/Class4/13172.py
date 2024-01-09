# 걸린 시간 : 30분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys

P = 1_000_000_007

# b ^ P-2 mod P 를 계산하기 위함. 분할정복으로 큰 P에 대해 빠르게 계산한다.
def power_mod(b, k):
    if k == 0:
        return 1
    elif k == 1:
        return b

    if k % 2 == 0:
        return (power_mod(b, k // 2) % P) ** 2 % P

    return ((power_mod(b, k - 1) % P) * b) % P


M = int(input())
N = []
S = []

for _ in range(M):
    n, s = map(int, sys.stdin.readline().split())
    N.append(n)
    S.append(s)

answer = 0
for i in range(M):
    N_reverse = power_mod(N[i], P-2) % P
    answer += (S[i] * N_reverse) % P
    answer %= P

print(answer)