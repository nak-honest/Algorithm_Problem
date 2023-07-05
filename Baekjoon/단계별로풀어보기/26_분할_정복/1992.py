import sys

N = int(input())
video = [list(map(int, input())) for _ in range(N)]

def compression(x, y, n):
    black_count = 0
    # 현재 부분의 1의 개수를 센다.
    for i in range(n):
        for j in range(n):
            black_count += video[x+i][y+j]

    if black_count == n ** 2:
        # 현재 부분이 1로만 채워져 있으면 1로 압축한다.
        print(1, end='')
        return

    elif black_count == 0:
        # 현재 부분이 0으로만 채워져 있으면 0으로 압축한다.
        print(0, end='')
        return

    half_n = n // 2

    print('(', end='')

    compression(x, y, half_n)                   # 왼쪽 위 부분 방문
    compression(x, y + half_n, half_n)          # 오른쪽 위 부분 방문
    compression(x + half_n, y, half_n)          # 왼쪽 아래 부분 방문
    compression(x + half_n, y + half_n, half_n) # 오른쪽 아래 부분 방문

    print(')', end='')


compression(0, 0, N)