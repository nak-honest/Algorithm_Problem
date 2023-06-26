# ASCII : chr(65) = 'A', chr(66) = 'B', ..., chr(90) = 'Z'
# alphabet_notation = {'A': 10, 'B': 11, ..., 'Z': 35}
alphabet_notation = {chr(c): ord(chr(c)) - 55 for c in range(65, 91)}
notation = {str(i): i for i in range(10)} | alphabet_notation

N, B = input().split()

# decimal = [N0 * B^0, N1 * B^1, ...]
decimal = [notation[N[-(i+1)]] * int(B)**i for i in range(len(N))]

print(sum(decimal))

# int()는 진법을 지정해서 숫자를 변환할 수 있다.
# print(int(N, int(B)))
