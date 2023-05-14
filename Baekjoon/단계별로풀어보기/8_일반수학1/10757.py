from collections import deque


A, B = map(deque, input().split())

# 자리 수를 맞추기 위해 앞에 0을 추가한다.
if len(A) > len(B):
    B.extendleft([0] * (len(A) - len(B)))
elif len(B) > len(A):
    A.extendleft([0] * (len(B) - len(A)))

answer = deque([])
carry = 0

# 뒤에서부터 한자리씩 더한다. 이때 앞에서 나온 carry도 같이 더한다.
# A나 B 중 길이가 더 짧은 자리 수에 맞춰서 더한다.
for _ in range(len(A)):
    addition = int(A[-1]) + int(B[-1]) + carry
    if addition >= 10:
        carry = 1
        addition -= 10
    else:
        carry = 0
    # A와 B의 마지막 자리의 수를 pop한다.
    A.pop()
    B.pop()

    answer.appendleft(addition)

# 마지막에 캐리가 발생했다면 이를 더한다.
if carry == 1:
    answer.appendleft(1)

print(*answer, sep='')
