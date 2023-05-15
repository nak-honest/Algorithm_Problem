from itertools import dropwhile

M, N = int(input()), int(input())
answer = []

for n in range(M, N + 1):
    if n != 1 and not list(dropwhile(lambda i: n % i != 0, range(2, n))):
        answer.append(n)

if answer:
    print(sum(answer), min(answer), sep='\n')
else:
    print(-1)