from collections import deque

while True:
    num = int(input())
    if num == 0:
        break

    dq = deque(str(num))

    while len(dq) > 1 and dq[0] == dq[-1]:
        dq.pop()
        dq.popleft()

    if len(dq) > 1:
        print("no")
    else:
        print("yes")
