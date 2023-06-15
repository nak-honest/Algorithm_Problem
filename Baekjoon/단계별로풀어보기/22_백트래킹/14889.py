import sys

N = int(input())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
team_num = N//2

# link 팀에서 한명씩 start team으로 이동 시킬 것이기 때문에 다음과 같이 초기화 한다.
start_team = [] # start팀 멤버들
link_team = dict.fromkeys([i for i in range(N)], 0) # link 팀 멤버들
start_stats = 0
link_stats = 0

# link 팀의 총 능력치 합을 구한다.
for i in range(N):
    for j in range(i+1, N):
        link_stats += S[i][j] + S[j][i]

min_diff = (N ** 2) * 50


def get_min_diff(depth, next):
    global start_stats, link_stats
    if promising():
        # start 팀과 link 팀이 반반으로 나뉘었으므로 min_diff를 업데이트 한다.
        if depth == team_num-1:
            global min_diff
            min_diff = min(min_diff, abs(start_stats - link_stats))
        else:
            # i를 0부터 돌리는게 아니라 next부터 돌린다는게 아주 중요하다.
            # 즉 start_team은 오름차순을 유지하도록 하면, 시간이 효율적이다.
            # [1, 3, 5]는 [3, 1, 5], [5, 1, 3], ... 이러한 팀과 같은 팀이다.
            for i in range(next, N):
                start_stats_backup = start_stats
                link_stats_backup = link_stats

                # start team에 i번 사람을 넣는다.
                for j in start_team:
                    start_stats += S[i][j] + S[j][i]
                start_team.append(i)

                # link team에서 i번 사람을 뺀다.
                link_team.pop(i)
                for j in link_team:
                    link_stats -= S[i][j] + S[j][i]

                # 재귀 호출
                get_min_diff(depth+1, i+1)

                # 재귀 호출이 끝나면 i번 사람을 start team에서 link team으로 이동시킨다.
                start_team.pop()
                link_team[i] = 0
                start_stats = start_stats_backup
                link_stats = link_stats_backup


def promising():
    # start 팀이 이미 link 팀보다 사람이 많은데, 능력치 차가 min_diff보다 큰 경우 재귀를 멈춘다.
    if start_stats - link_stats >= min_diff:
        return False

    return True


get_min_diff(-1, 0)
print(min_diff)