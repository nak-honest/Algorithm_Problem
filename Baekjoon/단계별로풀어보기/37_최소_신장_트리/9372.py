# 걸린 시간 : 10분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

import sys

# 노드의 개수가 N개인데, 모든 노드를 방문하려면 모든 노드들이 연결되어 있는 그래프여야 한다.
# 이때 연결되는 edge의 최소 개수는 N-1개이다.
for _ in range(int(input())):
    N, M = map(int, input().split())
    for _ in range(M):
        dummy = sys.stdin.readline()

    print(N-1)
