# LCS 기본 알고리즘과 동일하다.
# dp에 길이를 저장할때 그 길이에 해당하는 공통 부분 문자열도 함께 저장한다.

s1 = input()
s2 = input()

dp = [[[0, ''] for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
max_len = 0
answer = ''

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        # 길이 업데이트 시에는 문자열을 하나 덧붙인다.
        if s1[i-1] == s2[j-1]:
            dp[i][j][0] = dp[i-1][j-1][0] + 1
            dp[i][j][1] = dp[i-1][j-1][1] + s1[i-1]

            if max_len < dp[i][j][0]:
                max_len = dp[i][j][0]
                answer = dp[i][j][1]

        # 왼쪽이나 위에서 가져오는 경우에는 복사한다.
        elif dp[i-1][j][0] > dp[i][j-1][0]:
            dp[i][j][0] = dp[i-1][j][0]
            dp[i][j][1] = dp[i-1][j][1]
        else:
            dp[i][j][0] = dp[i][j-1][0]
            dp[i][j][1] = dp[i][j-1][1]

print(max_len)
print(answer)
