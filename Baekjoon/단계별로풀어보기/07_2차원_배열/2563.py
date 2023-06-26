paper = [[0 for _ in range(100)] for _ in range(100)]

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[i + x][j + y] = 1

print(sum(sum(paper, [])))
