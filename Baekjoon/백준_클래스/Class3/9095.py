# 3 * i + 2 * j + 1 * k

factorial = [1]
for i in range(1, 11):
    factorial.append(factorial[-1] * i)


for _ in range(int(input())):
    n = int(input())

    count = 0

    for i in range(n // 3 + 1):
        for j in range((n - 3 * i) // 2 + 1):
            k = n - 3*i - 2*j
            count += factorial[i + j + k] // (factorial[i] * factorial[j] * factorial[k])

    print(count)