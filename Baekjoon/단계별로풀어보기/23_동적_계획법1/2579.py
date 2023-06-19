# 다른 사람의 풀이와 살짝 다름.
# 다른 풀이는 i-3 -> i-1 -> i 와 i-2 -> i 둘 중 더 큰 값을 선택한다.
# 하지만 나의 풀이는 i-1 -> i와 i-2 -> i를 따로 저장해서 풀기 때문에 메모리를 더 사용한다는 단점이 있다.

import sys

n = int(input())
stairs = [int(sys.stdin.readline()) for _ in range(n)]

# i-1번째 계단을 오르고 바로 i번째 계단을 오른 경우의 최대 점수를 저장한다.
stairs_continous = stairs[:]

# i-2번째 계단을 오르고 i-1번째 계단은 오르지 않고 i번째 계단을 오른 경우의 최대 점수를 저장한다.
stairs_not_continous = stairs[:]

if n != 1:
    stairs_continous[1] += stairs_not_continous[0]

for i in range(2, n):
    stairs_continous[i] += stairs_not_continous[i-1] # 연속해서 올라가는 경우
    stairs_not_continous[i] += max(stairs_continous[i-2], stairs_not_continous[i-2]) # 한 칸 띄어서 올라가는 경우

print(max(stairs_continous[n-1], stairs_not_continous[n-1]))