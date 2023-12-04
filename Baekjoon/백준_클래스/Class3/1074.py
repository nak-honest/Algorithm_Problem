N, r, c = map(int, input().split())

length = 2 ** N
answer = length ** 2

while length > 1:
    length //= 2
    area_of_part = length ** 2
    if r >= length and c >= length:
        r -= length
        c -= length
    elif r >= length and c < length:
        answer -= area_of_part
        r -= length
    elif r < length and c >= length:
        answer -= area_of_part * 2
        c -= length
    else:
        answer -= area_of_part * 3

print(answer-1)

'''
answer : 2^2N
길이 : 2^N
4등분된 파트 넓이 : (길이/2) ^ 2
1. r >= 길이/2, c >= 길이/2 (오른쪽 밑)
    answer -= 0 
    r -= 길이/2
    c -= 길이/2
2. r >= 길이/2, c < 길이/2 (왼쪽 밑)
    answer -= 파트 넓이
    r -= 0
    c -= 길이/2
3. r < 길이/2, c >= 길이/2 (오른쪽 위)
    answer -= 2 * 파트 넓이
    r -= 0
    c -= 길이/2
4. r < 길이/2, c < 길이/2 (왼쪽 위) 
    answer -= 3 * 파트 넓이
    r -= 0
    c -= 0
    
이를 길이가 2일때까지만 반복을 한다.
'''