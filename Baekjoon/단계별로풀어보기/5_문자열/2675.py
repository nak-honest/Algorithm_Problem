n = int(input())

strings = [list(input().split()) for _ in range(n)]
answer = []

for s in strings:
    P = "".join([c*int(s[0]) for c in s[1]])
    answer.append(P)

print(*answer, sep='\n')