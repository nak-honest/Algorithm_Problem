import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))

increase = [1] * N # 부분 수열의 마지막 원소를 index가 i인 수로 했을때, 가장 긴 증가하는 부분 수열의 길이를 increase[i]에 저장한다.
decrease = [1] * N # 부분 수열의 시작 원소를 index가 i인 수로 했을때, 가장 긴 감소하는 부분 수열의 길이를 decrease[i]에 저장한다.

# 그러면 increase와 decrease를 합친게 가장 긴 바이토닉 부분 수열의 길이가 된다.

# increase를 처음부터 채운다.
for i in range(N):
    max_len = 0
    for j in range(i-1, -1, -1):
        if A[i] > A[j]:
            max_len = max(max_len, increase[j])
    increase[i] += max_len

# decrease를 끝에서부터 반대로 채운다.
for i in range(N-1, -1, -1):
    max_len = 0
    for j in range(i+1, N):
        if A[i] > A[j]:
            max_len = max(max_len, decrease[j])
    decrease[i] += max_len


answer = 0
for inc, dec in zip(increase, decrease):
    # increase와 decrease 모두 자기 자신을 포함하기 때문에 원소의 개수를 더할때 중복이 된다.
    # 따라서 1을 뺴주어야 한다.
    answer = max(answer, inc + dec - 1)
print(answer)