count = 0

'''
// 직접 재귀 돌리면 시간 초과 발생
// fib(n)을 만드는데 1을 몇번 더하냐는 것으로, 이는 결국 fib(n)의 값을 의미한다. 
def fib_rec(n):
    if n == 1 or n == 2:
        global count
        count += 1
        return 1
    return fib_rec(n-1) + fib_rec(n-2)
'''


def fib_dp(n):
    f = [1] * (n+1)
    for i in range(3, n+1):
        global count
        count += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]


n = int(input())
print(fib_dp(n), count)
