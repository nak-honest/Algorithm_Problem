import sys
N, M = map(int, input().split())

poketmon = {str(i): sys.stdin.readline().rstrip('\n') for i in range(1, N+1)}

for i in range(1, N+1):
    poketmon[poketmon[str(i)]] = i

for _ in range(M):
    print(poketmon[sys.stdin.readline().rstrip('\n')])