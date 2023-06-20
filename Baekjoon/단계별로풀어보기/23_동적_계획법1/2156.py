import sys


n = int(input())
wine = [int(sys.stdin.readline()) for _ in range(n)]
dp = wine[:]

if n > 3:
    dp[3] += max(wine[0] + wine[1], wine[0] + wine[2])
if n > 2:
    dp[2] += max(wine[0], wine[1])
if n > 1:
    dp[1] += wine[0]

# 계단 오르기 문제(2579)와 달리 i-4 -> i-1 -> i 인 경우도 존재한다. 두칸을 뛸수도 있기 때문이다.
# 하지만 세칸을 뛰는 것은 고려하지 않는다.
# 세칸을 뛰는 경우에는 가운데를 선택할수 있음에도 선택하지 않는것이기 때문에 최대 값이 될수 없다.
# i-4 -> i 인 경우는 i-4 -> i-2 -> i가 될수 있고, i-5 -> i-1 -> i 는 i-5 -> i-3 -> i-1 -> i 가 될수 있다.
for i in range(4, n):
    dp[i] += max(dp[i-2], dp[i-3] + wine[i-1], dp[i-4] + wine[i-1])

print(max(dp))