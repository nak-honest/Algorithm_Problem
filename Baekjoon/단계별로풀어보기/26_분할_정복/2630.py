import sys

N = int(input())
total_paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white_paper = 0 # 하얀색 색종이 수
blue_paper = 0  # 파란색 색종이 수

def split_paper(paper):
    blue_cell = 0 # 파란색 칸의 개수
    for row in paper:
        blue_cell += row.count(1)

    if blue_cell == len(paper) ** 2:
        # 파란색 칸의 개수가 paper의 1의 개수와 같다면 이 paper는 파란색 색종이이다.
        global blue_paper
        blue_paper += 1
    elif blue_cell == 0:
        # 파란색 칸의 개수가 0이라면 이 paper는 하얀색 색종이이다.
        global white_paper
        white_paper += 1
    else:
        # 파란색 칸과 흰색 칸이 섞여있으므로 paper를 잘라야한다.
        half = len(paper) // 2

        # paper를 4등분 한다.
        split_paper([row[:half] for row in paper[:half]]) # 왼쪽 위
        split_paper([row[half:] for row in paper[:half]]) # 오른쪽 위
        split_paper([row[:half] for row in paper[half:]]) # 왼쪽 아래
        split_paper([row[half:] for row in paper[half:]]) # 오른쪽 아래


split_paper(total_paper)
print(white_paper, blue_paper, sep='\n')