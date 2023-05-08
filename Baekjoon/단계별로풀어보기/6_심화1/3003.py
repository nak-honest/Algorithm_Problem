piece = [1, 1, 2, 2, 2, 8]
wrong = list(map(int, input().split()))

print(*[p-w for p, w in zip(piece, wrong)])