from collections import deque

T = int(input())

for _ in range(T):
    count = 0
    N, M = map(int, input().split())
    # priority에는 [(0, 우선순위), (2, 우선순위), ...] 이렇게 저장된다.
    priority = deque(enumerate(map(int, input().split())))

    for _ in range(N):
        # 우선순위가 가장 높은 아이템의 index를 찾는다.
        highest_index = priority.index(max(priority, key=lambda x: x[1]))
        priority.rotate(-highest_index)
        if priority[0][0] == M:
            print(count+1)
            break
        priority.popleft()
        count += 1