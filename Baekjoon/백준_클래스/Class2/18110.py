# 파이썬에서 round 함수는 .5에 대해 이상하게 동작한다....
# round(16.5)는 16이고, round(17.5)는 18이라고 한다...
# 올림값과 내림값의 딱 중간 값일 때에는 짝수값을 택한다고 한다..
# 따라서 이러한 경우에는 int(x + 0.5)로 계산하자.

import sys

n = int(input())

rank = [0] * 31

for _ in range(n):
    rank[int(sys.stdin.readline())] += 1

except_num = int(n * 0.15 + 0.5)

count = except_num
min_rank = 1
max_rank = 30

while count > 0:
    while rank[min_rank] == 0:
        min_rank += 1

    while rank[max_rank] == 0:
        max_rank -= 1

    rank[min_rank] -= 1
    rank[max_rank] -= 1

    count -= 1

answer = 0
for i in range(1, 31):
    answer += (i * rank[i])

if n == 0:
    print(0)
else:
    print(int(answer / (n - 2 * except_num) + 0.5))