import sys

N, M = map(int, input().split())
no_listen = {sys.stdin.readline().rstrip('\n') for _ in range(N)}
no_see = {sys.stdin.readline().rstrip('\n') for _ in range(M)}

no_listen_and_see = no_listen & no_see
print(len(no_listen_and_see), *sorted(no_listen_and_see), sep='\n')