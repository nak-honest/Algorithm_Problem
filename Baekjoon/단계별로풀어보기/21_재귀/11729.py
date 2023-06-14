def hanoi(n, source, destination, extra):
    if n == 1:
        s.append([source, destination])
        hanoi.count += 1
    else:
        hanoi(n-1, source, extra, destination)
        s.append([source, destination])
        hanoi.count += 1
        hanoi(n-1, extra, destination, source)

N = int(input())
s = []
hanoi.count = 0
hanoi(N, 1, 3, 2)

print(hanoi.count)
for i in range(hanoi.count):
    print(*s[i])
