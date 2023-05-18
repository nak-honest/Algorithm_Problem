N = int(input())

answer = 0
for n in range(N // 10, N):
    constructor = n + sum(map(int, str(n)))
    if constructor == N:
        answer = n
        break

print(answer)