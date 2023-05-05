N, X, *num = map(int, open(0).read().split())

answer = [n for n in num if n < X]
print(*answer)