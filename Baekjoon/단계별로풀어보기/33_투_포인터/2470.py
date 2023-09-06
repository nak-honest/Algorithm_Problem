import sys

N = int(input())
solutions = sorted(list(map(int, sys.stdin.readline().split())))

i = 0
j = N - 1

min_sum = sys.maxsize
answer = (solutions[i], solutions[j])

# 투포인터로 양쪽 끝에서 줄여가면서 합이 가장 작은 경우를 찾는다.
while i < j:
    solution_sum = solutions[i] + solutions[j]

    # 두 수의 합이 0에 얼만큼 가까운지를 보기 위해 절대값을 확인한다.
    if abs(solution_sum) < min_sum:
        answer = (solutions[i], solutions[j])
        min_sum = abs(solution_sum)

    if solution_sum == 0:
        break
    # 합이 0보다 크다면 그 합이 줄어들어야 한다는 것이다. 따라서 j를 1 감소시켜서 두 합을 줄인다.
    elif solution_sum > 0:
        j -= 1
    # 합이 0보다 작다면 그 합이 늘어나야 한다는 것이다. 따라서 i를 1 증가시켜서 두 합을 늘린다.
    elif solution_sum < 0:
        i += 1

print(*answer)
