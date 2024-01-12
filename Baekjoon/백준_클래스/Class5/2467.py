# 모든 용액이 알칼리 용액인 경우, 잘못된 인덱스를 저장하는 엣지 케이스를 신경쓰지 못함.

# 걸린 시간 : 30분
# 제출 횟수 : 6번
# 풀이 참조 : x
# 반례 참조 : x

import sys

N = int(input())
solid = list(map(int, sys.stdin.readline().split()))

acidic = len(solid)
alkaline = -1

for i in range(len(solid)):
    if solid[i] > 0:
        acidic = i
        if i > 0:
            alkaline = i-1
        break

if acidic == len(solid):
    alkaline = len(solid) - 1

min_sum = sys.maxsize
answer = solid[:2]

if acidic + 1 < len(solid):
    if min_sum > solid[acidic] + solid[acidic+1]:
        min_sum = solid[acidic] + solid[acidic+1]
        answer = [solid[acidic], solid[acidic+1]]

if alkaline - 1 >= 0:
    if min_sum > abs(solid[alkaline] + solid[alkaline-1]):
        min_sum = abs(solid[alkaline] + solid[alkaline-1])
        answer = [solid[alkaline-1], solid[alkaline]]

while acidic < len(solid) and alkaline >= 0:
    if min_sum > abs(solid[acidic] + solid[alkaline]):
        min_sum = abs(solid[acidic] + solid[alkaline])
        answer = [solid[alkaline], solid[acidic]]

    if min_sum == 0:
        break

    if solid[acidic] < abs(solid[alkaline]):
        acidic += 1
    else:
        alkaline -= 1

print(answer)