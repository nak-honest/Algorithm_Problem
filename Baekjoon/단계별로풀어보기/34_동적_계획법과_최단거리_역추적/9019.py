from collections import deque

def to_string(num):
    return "0" * (4 - len(str(num))) + str(num)


# 테스트 케이스의 개수가 매우 많기 때문에 각 연산의 결과를 캐싱한다.

D = {i: (2*i) % 10000 for i in range(10000)}

S = {i: i-1 for i in range(1, 10000)}
S[0] = 9999

L = {}
for i in range(10000):
    dq = deque(to_string(i))
    dq.rotate(-1)

    L[i] = int(''.join(dq))

R = {}
for i in range(10000):
    dq = deque(to_string(i))
    dq.rotate(1)

    R[i] = int(''.join(dq))


for _ in range(int(input())):
    A, B = map(int, input().split())

    q = deque()
    visited = [False] * 10000
    # 각 숫자에 도달하기 위해 필요한 직전의 연산과 이전 수를 저장한다.
    op_trace = [['', -1] for _ in range(10000)]

    q.append(A)
    visited[A] = True

    # bfs를 돌며 B에 도달하는 최단 경로를 찾는다.
    while q:
        node = q.popleft()

        if node == B:
            break

        rst_of_D = D[node]

        if not visited[rst_of_D]:
            q.append(rst_of_D)
            visited[rst_of_D] = True
            op_trace[rst_of_D] = ['D', node]


        rst_of_S = S[node]

        if rst_of_S == -1:
            rst_of_S = 9999

        if not visited[rst_of_S]:
            q.append(rst_of_S)
            visited[rst_of_S] = True
            op_trace[rst_of_S] = ['S', node]


        rst_of_L = L[node]

        if not visited[rst_of_L]:
            q.append(rst_of_L)
            visited[rst_of_L] = True
            op_trace[rst_of_L] = ['L', node]


        rst_of_R = R[node]

        if not visited[rst_of_R]:
            q.append(rst_of_R)
            visited[rst_of_R] = True
            op_trace[rst_of_R] = ['R', node]

        if rst_of_D == B or rst_of_S == B or rst_of_L == B or rst_of_R == B:
            break

    cur = B
    answer = deque()

    while cur != -1:
        answer.appendleft(op_trace[cur][0])
        cur = op_trace[cur][1]

    print(''.join(answer))