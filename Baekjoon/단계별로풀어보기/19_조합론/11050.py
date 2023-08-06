# nCr = (n-1)C(r-1) + (n-1)Cr 이라는 성질을 이용해 dynamic programming으로 풀이
# O(nk)라 팩토리얼을 사용하는 것보다 더 효율적이다.
n, k = map(int, input().split())
arr = [[1 for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    for j in range(1, k+1):
        if j != i:
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

print(arr[n][k])



'''
기본적인 factorial을 활용한 풀이
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


N, K = map(int, input().split())
print(fact(N) // (fact(K) * fact(N-K)))
'''