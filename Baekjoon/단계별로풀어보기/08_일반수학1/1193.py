from math import ceil

X = int(input())
n = ceil((2*X+0.25)**0.5-0.5)

index = X - n*(n-1)//2 - 1
part = [str(i) for i in range(1, n+1)]

if n % 2 == 0:
    print(part[index] + '/' + part[-(index + 1)])
else:
    print(part[-(index+1)] + '/' + part[index])