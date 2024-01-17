# 기존 방식은 계속해서 메모리 초과가 나서 해결하는데 오래 걸렸다.
# 기존에는 알칼리 두개를 합친 특성값과 산성 두개를 합친 특성값을 미리 모조리 구해서 정렬해 놓았기 떄문에 메모리가 부족했다.

# 걸린 시간 : 1시간
# 제출 횟수 : 7번
# 풀이 참조 : x
# 반례 참조 : x

import sys

N = int(input())

solutions = list(sorted(map(int, sys.stdin.readline().split())))

alkali = []
acid = []

acid_start = len(solutions)
for i in range(N):
    if solutions[i] > 0:
        acid_start = i
        break

alkali = []
if acid_start > 0:
    alkali = solutions[acid_start-1::-1]
acid = solutions[acid_start:]

min_sum = sys.maxsize
answer = []

if len(alkali) >= 3:
    min_sum = -(alkali[0] + alkali[1] + alkali[2])
    answer = alkali[2::-1]

if len(acid) >= 3 and min_sum > acid[0] + acid[1] + acid[2]:
    min_sum = acid[0] + acid[1] + acid[2]
    answer = acid[:3]

# 알칼리 용액 하나를 고정하고, 양쪽으로 투포인터 탐색
if len(alkali) >= 2 and acid:
    for mid_index in range(len(alkali)-1):
        alkali_index = mid_index + 1
        acid_index = 0

        while alkali_index < len(alkali) and acid_index < len(acid):
            if min_sum == 0:
                break

            solutions_sum = abs(alkali[alkali_index] + alkali[mid_index] + acid[acid_index])
            if min_sum > solutions_sum:
                min_sum = solutions_sum
                answer = [alkali[alkali_index], alkali[mid_index], acid[acid_index]]

            if -(alkali[alkali_index] + alkali[mid_index]) > acid[acid_index]:
                acid_index += 1
            else:
                alkali_index += 1

# 산성 용액 하나를 고정하고, 양쪽으로 투포인터 탐색
if len(acid) >= 2 and alkali:
    for mid_index in range(len(acid)-1):
        acid_index = mid_index + 1
        alkali_index = 0

        while alkali_index < len(alkali) and acid_index < len(acid):
            if min_sum == 0:
                break

            solutions_sum = abs(alkali[alkali_index] + acid[mid_index] + acid[acid_index])
            if min_sum > solutions_sum:
                min_sum = solutions_sum
                answer = [alkali[alkali_index], acid[mid_index], acid[acid_index]]

            if -alkali[alkali_index] > acid[mid_index] + acid[acid_index]:
                acid_index += 1
            else:
                alkali_index += 1

print(*sorted(answer))


# 기존 방식
'''
# 산성 2, 알칼리 1
# 산성 1, 알칼리 2
# 산성 3
# 알칼리 3

import sys

N = int(input())

solutions = list(sorted(map(int, sys.stdin.readline().split())))

alkali = []
acid = []

acid_start = len(solutions)
for i in range(N):
    if solutions[i] > 0:
        acid_start = i
        break

alkali = []
if acid_start > 0:
    alkali = solutions[acid_start-1::-1]
acid = solutions[acid_start:]

# 산성 용액 2개를 합친 특성값, 알칼리 용액 2개를 합친 특성값을 모아둔다.
alkali_sum = set()
acid_sum = set()

for i in range(len(alkali)):
    for j in range(i+1, len(alkali)):
        alkali_sum.add(alkali[i] + alkali[j])

for i in range(len(acid)):
    for j in range(i+1, len(acid)):
        acid_sum.add(acid[i] + acid[j])

alkali_sum = sorted(alkali_sum, reverse=True)
acid_sum = sorted(acid_sum)

# 기존에는 두 용액을 합친 특성값에 대해서 어떤 용액을 합쳤는지 dict로 관리헀지만, 그렇게 하면 메모리가 초과되었다.
# 따라서 마지막에 직접 두 용액의 합이 주어질 때, 어떤 용액 2개를 합쳤는지 직접 구하는 방식으로 바꾸었다.
has_two_alkali = False
has_two_acid = False
min_alkali_sum = 0
min_acid_sum = 0
min_alkali = 0
min_acid = 0

min_sum = sys.maxsize
answer = []

if len(alkali) >= 3:
    min_sum = -(alkali[0] + alkali[1] + alkali[2])
    answer = alkali[2::-1]

if len(acid) >= 3 and min_sum > acid[0] + acid[1] + acid[2]:
    min_sum = acid[0] + acid[1] + acid[2]
    answer = acid[:3]

# 알칼리 용액 2개, 산성 용액 1개를 고르는 경우
# 알칼리 용액 2개를 합친 특성값과 산성 용액의 특성값으로 투포인터 탐색을 한다.
if alkali_sum and acid:
    alkali_sum_index = 0
    acid_index = 0

    while alkali_sum_index < len(alkali_sum) and acid_index < len(acid):
        if min_sum == 0:
            break

        solutions_sum = abs(alkali_sum[alkali_sum_index] + acid[acid_index])
        if min_sum > solutions_sum:
            min_sum = solutions_sum
            has_two_alkali = True
            min_alkali_sum = alkali_sum[alkali_sum_index]
            min_acid = acid[acid_index]

        if -alkali_sum[alkali_sum_index] > acid[acid_index]:
            acid_index += 1
        else:
            alkali_sum_index += 1

# 산성 용액 2개, 알칼리 용액 2개를 고르는 경우
# 산성 용액 2개를 합친 특성값과 알칼리 용액의 특성값으로 투포인터 탐색을 한다.
if alkali and acid_sum:
    alkali_index = 0
    acid_sum_index = 0

    while alkali_index < len(alkali) and acid_sum_index < len(acid_sum):
        if min_sum == 0:
            break

        solutions_sum = abs(alkali[alkali_index] + acid_sum[acid_sum_index])
        if min_sum > solutions_sum:
            min_sum = solutions_sum
            has_two_alkali = False
            has_two_acid = True
            min_alkali = alkali[alkali_index]
            min_acid_sum = acid_sum[acid_sum_index]

        if -alkali[alkali_index] > acid_sum[acid_sum_index]:
            acid_sum_index += 1
        else:
            alkali_index += 1

if has_two_alkali:
    for i in range(len(alkali)):
        for j in range(i+1, len(alkali)):
            if alkali[i] + alkali[j] == min_alkali_sum:
                answer = [alkali[j], alkali[i], min_acid]
                break

if has_two_acid:
    for i in range(len(acid)):
        for j in range(i+1, len(acid)):
            if acid[i] + acid[j] == min_acid_sum:
                answer = [min_alkali, acid[i], acid[j]]
                break

print(*sorted(answer))
'''