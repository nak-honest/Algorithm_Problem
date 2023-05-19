N = int(input())

if (N % 5) % 3 == 0:
    print(N // 5 + (N % 5) // 3)
elif N > 5 and (N % 5 + 5) % 3 == 0:
    print(N // 5 - 1 + (N % 5 + 5) // 3)
elif N > 10 and (N % 5 + 10) % 3 == 0:
    print(N // 5 - 2 + (N % 5 + 10) // 3)
else:
    print(-1)