# 걸린 시간 : 25분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

from copy import deepcopy

def square_num(i, j):
    return 3 * (i//3) + j//3

is_find = False

# 순서대로 각 빈칸을 채우는데, 매번 각 행, 열, 정사각형에서 이미 채운 숫자인지를 확인한다.
# 만약 모든 숫자가 행, 열, 정사각형 모두에 겹친다면 백트래킹 한다.
def get_answer(empty_index):
    global is_find
    if is_find:
        return

    if empty_index == len(empty):
        for i in range(9):
            print(*answer[i], sep='')
        is_find = True

        return

    i, j = empty[empty_index]

    for num in range(1, 10):
        if num in row_set[i] or num in col_set[j] or num in square_set[square_num(i, j)]:
            continue

        answer[i][j] = num
        row_set[i].add(num)
        col_set[j].add(num)
        square_set[square_num(i, j)].add(num)

        get_answer(empty_index+1)

        row_set[i].remove(num)
        col_set[j].remove(num)
        square_set[square_num(i, j)].remove(num)


board = [list(map(int, list(str(input())))) for _ in range(9)]
answer = deepcopy(board)

# 채워야 할 빈칸의 인덱스를 모아둔다.
empty = []

# 각 행, 열, 정사각형에 채운 숫자들을 모아둔다.
row_set = [set() for _ in range(9)]
col_set = [set() for _ in range(9)]
square_set = [set() for _ in range(9)]

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            empty.append((i, j))
        else:
            row_set[i].add(board[i][j])
            col_set[j].add(board[i][j])
            square_set[square_num(i, j)].add(board[i][j])

get_answer(0)
