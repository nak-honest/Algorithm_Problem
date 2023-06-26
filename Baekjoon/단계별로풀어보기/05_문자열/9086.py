T, *strings = list(open(0).read().split())

answer = [s[0] + s[-1] for s in strings]
print(*answer, sep='\n')