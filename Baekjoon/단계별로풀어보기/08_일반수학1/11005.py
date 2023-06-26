# ASCII : chr(65) = 'A', chr(66) = 'B', ..., chr(90) = 'Z'
# alphabet_notation = ['A', 'B', ..., 'Z']
alphabet = [chr(c) for c in range(65, 91)]
notation = [str(i) for i in range(10)] + alphabet

N, B = map(int, input().split())
answer = ''

while N > 0:
    digit = N % B
    N //= B
    answer += notation[digit]

print(*reversed(answer), sep='')


'''
# 복잡하게 푼 풀이
# 평소에 10진수를 B진수로 바꾸는 계산 방식이 복잡했는데 더 간단한 방식을 알게 되었다.
# 10진수를 N진수로 변환하는 방법은 매번 10진수를 N으로 나누면서 나머지로 자리수를 채우면 된다.

from math import log

# ASCII : chr(65) = 'A', chr(66) = 'B', ..., chr(90) = 'Z'
# alphabet_notation = ['A', 'B', ..., 'Z']
alphabet = [chr(c) for c in range(65, 91)]
notation = [str(i) for i in range(10)] + alphabet

N, B = map(int, input().split())

highest_degree = int(log(N, B))
answer = ['0' for _ in range(highest_degree+1)]

while N > 0:
    degree = int(log(N, B))

    for k in range(B + 1):
        if B ** degree * k > N:
            answer[-(degree+1)] = notation[k - 1]
            N -= B ** degree * (k - 1)
            break

print(*answer, sep='')
'''
