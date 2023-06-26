N, K = map(int, input().split())
m = []

for i in range(1, N+1):
    if N % i == 0:
        m.append(i)
    if len(m) == K:
        print(i)
        break

if len(m) < K:
    print(0)