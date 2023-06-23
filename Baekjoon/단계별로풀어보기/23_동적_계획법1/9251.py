# DP 문제에 많이 약한 것 같다. DP에서 테이블을 그릴 생각을 왜 못했을까? 결국 풀지 못하였다.
# 앞으로의 문제에서는 2차원 테이블을 그려보자. 테이블을 그려가면서 점화식을 찾아보자.

A = input()
B = input()
# dp[i][j]는 A[:i]와 B[:j]의 최장 공통 부분 수열의 길이를 저장한다. 이때 A[:i]는 A[0] ~ A[i-1]을 의미한다. 인덱스 주의!
dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
max_len = 0

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            # A[i]와 B[j]가 같을때 그 문자를 c라고 해보자.(즉 c == A[i] == B[j])
            # 그러면 A와 B에 c를 추가하기 전, 즉 A[:i]와 B[:j]의 최장 공통 부분 수열에 c를 추가한 것이
            # A[:i+1]과 B[:j+1]의 최장 공통 부분 수열이 된다.
            # 따라서 다음과 같은 점화식이 나오는 것이다.
            dp[i+1][j+1] = dp[i][j] + 1
            max_len = max(max_len, dp[i+1][j+1])
        else:
            # A[i]와 B[j]가 다른 경우에는 해당 문자를 추가한다고 최장 공통 부분 수열의 길이가 늘어나지는 않는다.
            # A[i]를 a라 하고 B[j]를 b라고 할때 a와 b 둘다 추가하지 않은 상태에서
            # a만 추가했을 때의 LCS 길이와 b만 추가했을 떄의 LCS 길이 중 더 큰 길이가 a와 b를 둘다 추가했을 때의 LCD 길이이다.
            # 왜냐하면 a와 b가 다르기 때문에 둘다 추가한다고 해서 LCS의 길이가 늘어나지 않기 때문이다.
            # 따라서 다음과 같은 점화식이 나오는 것이다.
            # a만 추가했을 때의 LCS 길이가 dp[i+1][j]이고 b만 추가했을 때의 LCS 길이가 dp[i][j+1] 이다.
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(max_len)

'''
# 처음에는 dp[i]에 A[i]를 부분 수열의 끝으로 하였을 때 가장 긴 길이를 저장시켰고
# B_index에는 해당 부분 수열의 마지막이 B의 어느 인덱스에 있는지를 저장시켰다.
# 그런데 이렇게 하면 정답이 아니다.
# 예를들어 A = ACAPK, B = CAPKCA 라고 하면 CAPK가 가장 긴 부분 수열이라 4가 나와야 하지만 3이 나온다.
# 그렇게 되는 이유는 dp[1]에는 AC가 있기 때문에 2가 저장되고, dp[2]에는 ACA가 있기 때문에 3이 저장되기 때문이다.
# 즉 dp[1]은 AC 패턴에 대한 것이기 때문에 B_index[1]에 4를 저장하고 dp[2]는 ACA 패턴에 대한 것이기 때문에 B_index[2]에 5를 저장하는데,
# 이렇게 되면 A[3]를 끝으로 하는 부분수열을 찾을때 ACP와 ACAP가 B에 있는지를 찾게된다.
# 하지만 실제 정답은 CAPK 이므로 정답이 틀리게된다. 즉 dp[1]과 dp[2]가 저장하고 있는 패턴에서 맨 앞 A를 제거해야 한다는 것이다.

# 즉 dp[i]는 0부터 i까지 중에서 가장 긴 부분 수열의 길이를 저장하지만, dp[i+j]는 dp[i]의 부분 수열중 일부만 취해야 하는 경우도 있기 때문에 틀린 것이다.

A = input()
B = input()

dp = [1] * len(A)
B_index = [-1 for _ in range(len(A))]

for i in range(len(A)):
    max_len = 0
    max_B_index = -1
    for j in range(i-1, -1, -1):
        if max_len < dp[j]:
            new_B_index = B.find(A[i], B_index[j] + 1)
            if new_B_index != -1:
                max_B_index = new_B_index
                max_len = dp[j]

    if max_len > 0:
        dp[i] += max_len
        B_index[i] = max_B_index
    else:
        B_index[i] = B.find(A[i])

print(max(dp))
'''