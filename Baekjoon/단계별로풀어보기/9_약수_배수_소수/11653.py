N = int(input())

for i in range(2, N+1):
    if N == 1:
        break
    while N % i == 0:
        print(i)
        N //= i