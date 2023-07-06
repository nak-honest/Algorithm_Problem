import sys

N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

minus_paper = 0
zero_paper = 0
plus_paper = 0


def slice_paper(x, y, n):
    minus_count = 0
    zero_count = 0
    plus_count = 0

    # 이 종이의 숫자 개수를 센다.
    for i in range(n):
        minus_count += paper[x+i][y:y+n].count(-1)
        zero_count += paper[x+i][y:y+n].count(0)
        plus_count += paper[x+i][y:y+n].count(1)

    n_square = n ** 2
    if minus_count == n_square:
        # 이 종이는 -1로만 채워져 있는 종이이다.
        global minus_paper
        minus_paper += 1
        return

    if zero_count == n_square:
        # 이 종이는 0으로만 채워져 있는 종이이다.
        global zero_paper
        zero_paper += 1
        return

    if plus_count == n_square:
        # 이 종이는 1로만 채워져 있는 종이이다.
        global plus_paper
        plus_paper += 1
        return

    n_div = n // 3

    # 종이를 9조각으로 쪼갠다.
    slice_paper(x, y, n_div)
    slice_paper(x, y+n_div, n_div)
    slice_paper(x, y+n_div*2, n_div)

    slice_paper(x+n_div, y, n_div)
    slice_paper(x+n_div, y+n_div, n_div)
    slice_paper(x+n_div, y+n_div*2, n_div)

    slice_paper(x+n_div*2, y, n_div)
    slice_paper(x+n_div*2, y+n_div, n_div)
    slice_paper(x+n_div*2, y+n_div*2, n_div)


slice_paper(0, 0, N)

print(minus_paper, zero_paper, plus_paper, sep='\n')