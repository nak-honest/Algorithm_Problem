import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))

DP = [1] * N # index i의 수를 시작으로 했을때 가장 긴 증가하는 부분 수열의 길이를 dp[i]에 저장한다.

# 끝에서부터 반대로 DP를 채운다.
for i in range(N-1, -1, -1):
    max_len = 0
    for j in range(i+1, N):
        if A[i] < A[j] and max_len < DP[j]:
            max_len = DP[j]

    DP[i] += max_len

print(max(DP))