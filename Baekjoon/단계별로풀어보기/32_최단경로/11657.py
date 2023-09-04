# 오랜만에 보니 벨만포드 알고리즘이 하나도 기억이 안났다.
import sys

def add(a, b):
    if a == sys.maxsize or b == sys.maxsize:
        return sys.maxsize
    return a + b

# 음의 사이클이 있는지 확인한다.
def is_negative_cycle(destination, adj):
    for node in range(1, N+1):
        for next, dest in adj[node]:
            if add(destination[node], dest) < destination[next]:
                return True
    return False


N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    adj_list[A].append((B, C))

# 벨만 포드 알고리즘으로 최단 경로를 찾는다.
cur_dest = [sys.maxsize] * (N+1)
cur_dest[1] = 0

for _ in range(N-1):
    for node in range(1, N+1):
        for next, dest in adj_list[node]:
            if add(cur_dest[node], dest) < cur_dest[next]:
                cur_dest[next] = add(cur_dest[node], dest)

if is_negative_cycle(cur_dest, adj_list):
    print(-1)
else:
    for i in range(len(cur_dest)):
        if cur_dest[i] == sys.maxsize:
            cur_dest[i] = -1

    print(*cur_dest[2:], sep='\n')
