N, M = map(int, input().split())
how_to_reverse = [list(map(int, input().split())) for _ in range(M)]

answer = [i for i in range(1, N+1)]

for row in how_to_reverse:
    i, j = row
    answer[i-1:j] = reversed(answer[i-1:j])

print(*answer)