# 재귀 호출이 끝나면 해당 칸을 다시 0으로 설정해야 한다는 것을 정말 뒤늦게 알아차렸다.
# 그 이외에도 여전히 pypy3로만 통과하고 python3로는 시간초과가 발생한다.

import sys

sdoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
fill_index = []

for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            fill_index.append((i, j))

fill_num = len(fill_index)
is_end = False


def solve_sdoku(depth):
    if promising(depth):
        if depth == fill_num-1:
            global is_end
            is_end = True
            for line in sdoku:
                print(*line)

        else:
            i, j = fill_index[depth+1]
            for n in range(1, 10):
                sdoku[i][j] = n
                solve_sdoku(depth + 1)

            # 재귀 호출이 끝났으면 다시 0으로 설정해야 한다. 그렇지 않으면 9가 저장 되어서 문제가 발생하게 된다.
            sdoku[i][j] = 0


def promising(depth):
    if depth < 0:
        return True
    if is_end:
        return False

    i, j = fill_index[depth]
    new_num = sdoku[i][j]

    for row in range(9):
        if row != i and new_num == sdoku[row][j]:
            return False

    for col in range(9):
        if col != j and new_num == sdoku[i][col]:
            return False

    row = (i // 3) * 3
    col = (j // 3) * 3

    for r in range(3):
        for c in range(3):
            if (row + r != i or col + c != j) and sdoku[row+r][col+c] == new_num:
                return False

    return True


solve_sdoku(-1)

