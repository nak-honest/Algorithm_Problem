# 에라토스테네스의 체를 사용하면 훨씬 효율적으로 풀린다. 기말 끝나면 그렇게 풀어보자.

M, N = map(int, input().split())

if M <= 2:
    print(2)
    M = 3
if M == 3 and N != 2:
    print(3)
    M = 4

for n in range(M, N+1):
    sqrt = int(n**0.5)
    for i in range(2, sqrt+1):
        if n % i == 0:
            break
        if i == sqrt:
            print(n)
