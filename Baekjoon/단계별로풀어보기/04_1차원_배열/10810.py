N, M = map(int, input().split())
how = [list(map(int, input().split())) for _ in range(M)]

answer = [0 for _ in range(N)]

for row in how:
    i, j, k = row
    answer[i-1:j] = [k]*(j-i+1)

print(*answer)