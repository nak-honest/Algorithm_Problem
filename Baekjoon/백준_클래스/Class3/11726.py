fact = [1]
for i in range(1, 1001):
    fact.append(fact[-1]*i)

n = int(input())

answer = 0
for i in range(n//2 + 1):
    answer += fact[n-i] // (fact[n-2*i] * fact[i])
    answer %= 10007

print(answer)