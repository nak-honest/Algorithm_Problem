# 걸린 시간 : 40분
# 제출 횟수 : 2번
# 풀이 참조 : x
# 반례 참조 : x

N = int(input())

count = 0
for k in range(11):
    if 2 ** k == N // 3:
        count = k + 1
        break

left_star_position = set([(0, 0)])

for c in range(2, count + 1):
    new_left_star_position = set()
    added_position = [(0, 0), (0, 6 * (2 ** (c - 2))), (3 * (2 ** (c - 2)), 3 * (2 ** (c - 2)))]
    for i, j in left_star_position:
        for add_i, add_j in added_position:
            new_left_star_position.add((i + add_i, j + add_j))

    left_star_position = new_left_star_position.copy()

left_star_position = {(-(h - (N - 1)), j) for h, j in left_star_position}
added_position = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (-1, 1), (-1, 3), (-2, 2)]
board = [[False] * (N*2) for _ in range(N)]

for i, j in left_star_position:
    for add_i, add_j in added_position:
        board[i + add_i][j + add_j] = True

for i in range(N):
    # join으로 출력해야 시간 초과가 안난다. 하나 하나 출력하면 시간 초과 발생.
    line = []
    for j in range(N*2):
        if board[i][j]:
            line.append("*")
        else:
            line.append(" ")
    print("".join(line))

'''
단위 삼각형의 가장 왼쪽 밑의 좌표만 추적한다.
-> 가장 왼쪽 밑의 좌표가 (i, j)라면
[(i, j), (i, j+1), (i, j+2), (i, j+3), (i, j+4), (i-1, j+1), (i-1, j+3), (i-2, j+2)]
가 *의 위치가 된다.

가장 왼쪽 밑 삼각형에서 시작한다.
-> 가장 밑을 높이 0으로 설정하고, 이후에 뒤집어서 i를 구하면 된다.

처음에는 (0, 0) 한개
두번째는 (0, 0)을 오른쪽, 위로 옮기면 [(0, 0), (0, 6), (3, 3)]
세번째는 [(0, 0), (0, 6), (3, 3)]를 오른쪽, 위로 옮긴다.
(0, 0)만 생각하면 (0, 12), (6, 6) 이 된다.
네번째는 (0, 24), (12, 12)

i번째는 (0, 6 * 2 ^ (i-2)) 와 (3 * 2 ^(i-2), 3 * 2 ^(i-2)) 가 된다.
'''