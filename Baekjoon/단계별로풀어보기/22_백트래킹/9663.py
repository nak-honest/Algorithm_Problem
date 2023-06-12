# pypy3로 제출해야 시간 초과가 나지 않는다.
# 시험 끝나면 python3로 통과해보기.

N = int(input())
count = 0
# 각 열에 퀸을 하나씩만 놓을 수 있다. col은 퀸을 i 열의 몇번째 칸에 놓을지 저장한다.
col = [0 for _ in range(N)]


def nqueens(i):
    if(promising(i)):
        if i == N-1:
            global count
            count += 1
        else:
            for n in range(N):
                col[i+1] = n
                nqueens(i+1)


def promising(i):
    for j in range(i):
        # 같은 행에 있는 경우
        if col[i] == col[j]:
            return False
        # 같은 대각선에 있는 경우
        if col[i] == col[j] + (i - j) or col[i] == col[j] - (i - j):
            return False
    return True


nqueens(-1)
print(count)
