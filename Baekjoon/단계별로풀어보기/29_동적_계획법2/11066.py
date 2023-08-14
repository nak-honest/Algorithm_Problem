# 거의 다 접근했는데, dp를 1차원으로밖에 생각하지 못했다.
# 나는 dp[i] 를 0~i까지를 합쳤을때의 최소 비용으로 생각했는데, 정해는 2차원 dp로 풀어야 한다.
# 즉 dp[i][j] 를 i~j 까지를 합쳤을때의 최소 비용으로 풀어야 한다.

# 그리고 이 문제는 python3로는 통과가 안되고 pypy3로만 통과된다.
# 크누스 최적화 기법을 사용하면 python3로도 통과된다고 한다.
# 하지만 C++은 그냥 통과한다.. 역시 C++도 해야한다.

import sys

# start ~ end 까지의 구간합 = s[start] - s[end-1]
def addRange(s, start, end):
    if start == 0:
        return s[end]

    return s[end] - s[start-1]


T = int(input())

for _ in range(T):
    K = int(input())
    novels = list(map(int, sys.stdin.readline().split()))
    dp = [[0] * K for _ in range(K)]

    s = novels[:]
    for i in range(1, K):
        s[i] += s[i-1]

    # for문을 돌며 dp[j][j+i]를 구한다. 즉 j ~ j+i 를 합쳤을때의 최소비용을 구한다.
    # 이때 i가 1이 증가할때마다 합치는 범위가 1씩 증가한다.
    # j ~ j+i 를 합치는 경우의 수는
    # j ~ j 와 j+1 ~ j+i 를 더한다.
    # j ~ j+1 와 j+2 ~ j+i 를 더한다.
    # ...
    # j ~ j+i-1 와 j+i ~ j+i 를 더한다.
    # 이렇게 존재한다. 이중 최소가 되는 코스트가 dp[j][j+i]가 된다.
    for i in range(1, K):
        for j in range(K-i):
            min_cost = sys.maxsize
            for k in range(i):
                # j ~ j+k 와 j+k+1 ~ j+i를 더할때, dp의 값만 더하면 안된다.
                # dp는 누적 비용을 의미하고, 이 누적 비용에 누적된 두 수를 더하는 비용이 추가되어야 한다.
                # 그값은 (j ~ j+k 까지의 구간합) + (j+k+1 ~ j+i 까지의 구간합) 이다.
                new_cost = dp[j][j+k] + dp[j+k+1][j+i] + addRange(s, j, j+k) + addRange(s, j+k+1, j+i)
                min_cost = min(min_cost, new_cost)

            dp[j][j+i] = min_cost

    print(dp[0][K-1])


'''
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
'''