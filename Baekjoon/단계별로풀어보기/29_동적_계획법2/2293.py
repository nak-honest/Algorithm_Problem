# 다음과 같이 2차원 dp 점화식까지는 구할 수 있었다.
# dp[i][k] = dp[i-1][k] + dp[i-1][k-wi] + dp[i-1][k-2*wi] + ... + dp[i-1][k-x*wi]
# 하지만 메모리 초과가 발생하기 때문에 1차원 dp로 바꾸어야 하는데, 이 부분이 어려웠다.

import sys

N, K = map(int, input().split())
# dp[i][k]에서 i에 대한 값을 따로 2차원으로 저장하지 않고, for문을 돌면서 i가 1씩 증가하는 방식으로 구현한다.
# 즉 for문이 돌면서 사용할 수 있는 동전이 하나씩 늘어나게 되고, 그 동전들을 가지고 i원을 만들수 있는 경우의 수를 dp[i]에 저장한다.
dp = [0] * (K + 1)
dp[0] = 1

for _ in range(N):
    # 사용할 수 있는 동전이 하나씩 추가된다.
    coin = int(sys.stdin.readline())
    # 사용할 수 있는 동전이 하나씩 추가될때마다 dp의 값을 모두 업데이트 한다.
    for i in range(K+1):
        # 처음에는 2차원 dp에서 구한것처럼 dp[i] += (dp[i - coin] + dp[i - 2*coin] + ... + dp[i - j*coin])으로 정의했다.
        # 그랬더니 너무 숫자가 높게 나왔다!!
        # 다시 생각해보면 dp[i - 2*coin]를 더한다는 것의 의미는 coin 2개 + (i - 2*coin) 원을 만드는 경우의 수를 더한다는 것인데,
        # 이는 dp[i - coin] 에 포함되어 있기 때문에 중복이 된다.
        # dp[i - coin]에는 dp[i - coin - coin]를 더하게 되고, coin 1개 + (i - coin - coin) 원을 만드는 경우의 수를 더한다는 것이 된다.
        # 따라서 dp[i]에는 dp[i - coin]만 더하면 된다는 것을 알수 있다.
        # dp[i- coin]에는 dp[i - 2*coin]이 더해져 있고, dp[i - 2*coin]에는 dp[i - 3*coin]이 더해져 있기 때문에
        # dp[i]에 dp[i-coin]만 더해도 (dp[i - coin] + dp[i - 2*coin] + ... + dp[i - j*coin])를 전부 더한 것이 된다.
        # 쉽게 말해서 dp[i]에는 누적합이 저장된다는 것이다. 실제로 이렇게 하는 방법 대신 for i in range(K, 0, -1): 로 돌리고
        # (dp[i - coin] + dp[i - 2*coin] + ... + dp[i - j*coin])를 전부 더해도 정답이 되지만, 누적합이 아닌 하나씩 더하기때문에
        # 시간초과가 발생하게 된다.
        if i - coin >= 0:
            dp[i] += dp[i-coin]
print(dp[K])
