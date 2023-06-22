# 처음에는 많이 꼬인 선부터 제거하는 방식으로 풀었는데 틀렸다.
# 가장 많이 꼬인 선이 여러개일 어떤 선을 없애냐에 따라 결과가 다르기 때문이다.
# 다른 추가적인 기준도 적용시켜 보았지만 결국 풀리지 않았다.

# A와 B가 매핑된 테이블이 있다고 하면, A가 정렬되어 있을때 B가 정렬되어야 한다는 것을 생각하지 못했다.
# 더 나아가 B가 정렬되어야 하므로 정렬되지 못하게 하는 전기줄들을 없애야 하는데,
# 없애는 전기줄의 개수를 최소화 한다는 것은 결국 정렬된 부분 수열의 길이가 최대로 되도록 하는 것이다. 즉 LIS 의 길이를 구하는 문제이다.
# 진짜 생각지도 못했다... LIS 관련 문제 더 풀어보고 유형을 익히자.

import sys

n = int(input())

wires = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
B = [wire[1] for wire in sorted(wires, key=lambda x: x[0])]

DP = [1] * n
for i in range(n-1, -1, -1):
    max_len = 0
    for j in range(i+1, n):
        if B[i] < B[j]:
            max_len = max(max_len, DP[j])
    DP[i] += max_len

print(n - max(DP))