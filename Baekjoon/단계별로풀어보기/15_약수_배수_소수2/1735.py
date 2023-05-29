A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

A3 = A2*B1 + A1*B2
B3 = B1*B2

m = max(A3, B3)
n = min(A3, B3)

while m % n != 0:
    m, n = n, m%n

print(A3 // n, B3 // n)