N, M = map(int, input().split())
swap = [list(map(int, input().split())) for _ in range(M)]

answer = [i for i in range(1, N+1)]

for row in swap:
    i, j = row
    # i번은 index i-1을 의미한다. 1번부터 시작하기 떄문이다.
    answer[i-1], answer[j-1] = answer[j-1], answer[i-1]

print(*answer)

