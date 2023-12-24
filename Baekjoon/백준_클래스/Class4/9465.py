'''
    위 아래 중 하나를 택한뒤
    1. 그 다음에 반대쪽을 택한다.
    2. 그 다음에 택하지 않고, 다다음에 반대쪽을 택한다.
'''

import sys

for _ in range(int(input())):
    n = int(input())
    sticker = []
    sticker.append(list(map(int, sys.stdin.readline().split())))
    sticker.append(list(map(int, sys.stdin.readline().split())))

    if n >= 2:
        # dp[0][i]는 i열에서 위의 스티커를 선택했을 때의 최대값이고, dp[1][i]는 i열에서 아래의 스티커를 선택했을 때의 최대값이다.
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]
        dp[0][1] = dp[1][0] + sticker[0][1]
        dp[1][1] = dp[0][0] + sticker[1][1]

        for i in range(2, n):
            '''
            i열에서 위의 스티커를 선택했을 때의 최대 값은 다음 두 경우 중 하나이다.
            1. i-1열에서 밑의 스티커를 선택한 경우
            2. i-1열에서 아무 스티커도 선택하지 않고 i-2열에서 밑의 스티커를 선택힌 경우
            
            이는 i열에서 밑의 스티커를 선택했을 때의 최대값도 동일하게 적용된다.
            '''
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]

        print(max(dp[0][-1], dp[1][-1]))
    elif n == 1:
        print(max([sticker[0][0], sticker[1][0]]))