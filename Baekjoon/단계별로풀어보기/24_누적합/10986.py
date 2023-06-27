import sys

N, M = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))

# S[i]는 0~i 까지의 합을 M으로 나눈 나머지를 저장한다.
S = [0]

for num in A:
    S[-1] = (S[-1] + num) % M
    S.append(S[-1])
S.pop()

# count() 함수를 사용하면 매번 모든 원소를 뒤지기 때문에 시간 초과가 발생한다.
# 따라서 dict나 list를 통해 O(n)으로 모든 원소의 count를 미리 구해야 한다.
count_dict = {i: 0 for i in range(M)}

for num in S:
    count_dict[num] += 1

# S[i]가 0이라는 것은 0~i까지의 합이 이미 M으로 나누어 떨어진다는 이야기이다.
# 따라서 S에 저장된 0의 개수를 먼저 저장한다.
count = count_dict[0]

# S[i]와 S[j]가 같다면(i < j), 즉 0~i 까지의 합을 나눈 나머지와 0~j 까지의 합을 나눈 나머지가 같다면
# Ai ~ Aj을 더한 값은 M으로 나누어 떨어진다.
for i in range(M):
    count += count_dict[i] * (count_dict[i] - 1) // 2

print(count)
