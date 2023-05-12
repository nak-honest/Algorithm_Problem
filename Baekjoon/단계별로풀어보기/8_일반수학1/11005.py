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
