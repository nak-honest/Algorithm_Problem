ROW1 = ['W', 'B'] * 4
ROW2 = ['B', 'W'] * 4
CHESS_BOARD_1 = [ROW1, ROW2] * 4
CHESS_BOARD_2 = [ROW2, ROW1] * 4
N, M = map(int, input().split())
BOARD = [list(input()) for _ in range(N)]

# 보드에서 8x8 크기의 일 부분을 받아서 체스판으로 만드려고 할때 칠해야하는 개수를 반환한다.
def get_paint_num(board_part):
    diff1 = [CHESS_BOARD_1[i][j] != board_part[i][j] for i in range(8) for j in range(8)]
    diff2 = [CHESS_BOARD_2[i][j] != board_part[i][j] for i in range(8) for j in range(8)]
    return min(diff1.count(True), diff2.count(True))

min_paint = 64

# 보드에서 8X8 크기의 일 부분을 구해서 칠해야 하는 개수를 구한다.
# 그중 가장 작은 값을 찾아서 출력한다.
for right in range(N-7):
    for down in range(M-7):
        board_part = [[BOARD[right+i][down+j] for j in range(8)] for i in range(8)]
        min_paint = min(get_paint_num(board_part), min_paint)

print(min_paint)