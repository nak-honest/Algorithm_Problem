N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

answer = [list(map(lambda x, y: x + y, a, b)) for a, b in zip(A, B)]

for row in answer:
    print(*row)
