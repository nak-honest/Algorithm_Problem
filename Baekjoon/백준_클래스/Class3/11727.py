'''
2 -> 2가지 방법
1 -> 1가지 방법
'''

fact = [1]
for i in range(1, 1001):
    fact.append(fact[-1] * i)

n = int(input())
answer = 0

for two_count in range(n//2 + 1):
    one_count = n - 2 * two_count

    count = fact[n-two_count] // (fact[one_count] * fact[two_count])
    count *= (2 ** two_count)
    answer += count
    answer %= 10007

print(answer)
