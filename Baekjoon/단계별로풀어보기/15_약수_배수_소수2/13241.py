A, B = map(int, input().split())

m = max(A, B)
n = min(A, B)

while n != 0:
    m, n = n, m%n

# m은 두 수의 최대 공약수이다.
print(A*B//m)