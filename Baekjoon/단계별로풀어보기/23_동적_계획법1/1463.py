# Top-Down 방식의 DP가 훨씬 효율적인데, DP가 아닌 백트래킹으로 문제를 해결했다. 
# 메모이제이션을 연산 결과로 저장하려 해서 잘 풀리지 않았다.
min_count = 1000000


def make_one(n, count):
    if promising(count):
        if n == 1:
            global min_count
            min_count = min(count, min_count)
        elif n % 3 != 0 and n % 2 != 0:
            make_one(n - 1, count + 1)
        elif n % 3 == 0 and n % 2 != 0:
            make_one(n // 3, count + 1)
            make_one(n - 1, count + 1)
        elif n % 3 != 0 and n % 2 == 0:
            make_one(n // 2, count + 1)
            make_one(n - 1, count + 1)
        else:
            make_one(n // 3, count + 1)
            make_one(n // 2, count + 1)


def promising(count):
    if count >= min_count:
        return False
    return True


N = int(input())

make_one(N, 0)
print(min_count)


'''
# bottom-up 방식
# 나는 DP로 접근할때 계속 연산의 결과를 저장시키도록 풀었는데, 연산 횟수를 저장하도록 풀어야 한다.
N = int(input())

DP = [0] * (N+1) # DP[i]는 i를 1로 만드는데 필요한 연산의 최소값을 저장한다.

for i in range(2, N+1):
    DP[i] = DP[i-1] + 1
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i//2] + 1)
    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i//3] + 1)

print(DP[N])
'''

'''
# top-down 방식
# 가장 빠르게 풀린다.
N = int(input())

DP = [0] * (N+1)
def make_one(n):
    if n == 1:
        return 0
    if DP[n] != 0:
        return DP[n]

    if n % 2 != 0 and n % 3 != 0:
        DP[n] = make_one(n-1) + 1
    elif n % 2 != 0:
        DP[n] = min(make_one(n-1), make_one(n//3)) + 1
    elif n % 3 != 0:
        DP[n] = min(make_one(n-1), make_one(n//2)) + 1
    else:
        DP[n] = min(make_one(n//2), make_one(n//3)) + 1

    return DP[n]


make_one(N)
print(DP[N])
'''
