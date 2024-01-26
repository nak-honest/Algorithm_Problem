def ccw(a, b, c):
    return a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

P1 = tuple(map(int, input().split()))
P2 = tuple(map(int, input().split()))
P3 = tuple(map(int, input().split()))

D = ccw(P1, P2, P3)

if D > 0:
    print(1)
elif D < 0:
    print(-1)
else:
    print(0)
