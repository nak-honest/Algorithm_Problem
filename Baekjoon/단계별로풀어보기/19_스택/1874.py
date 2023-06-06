# 생각보다 어려웠다..

import sys
from collections import deque

N = int(input())

# seq는 문제에서 주어지는 수열인데 queue로 동작한다.
seq = deque([int(sys.stdin.readline()) for _ in range(N)])
stack = deque()

# nums는 1부터 n까지 정렬된 queue로 동작한다.
nums = deque([i for i in range(1, N+1)])
answer = []


while seq:
    # num가 비어있지 않다면 nums를 deque 후 stack에 넣는다. stack에 정렬된 순서로 넣어야 하기 때문이다.
    if nums:
        i = nums.popleft()
        if i <= seq[0]:
            stack.append(i)
            answer.append('+')
        # stack에 넣은 후 stack의 top과 seq의 front가 같다면, 두 값이 같지 않을때까지 계속 pop, dequeue를 한다.
        while stack and stack[-1] == seq[0]:
            stack.pop()
            seq.popleft()
            answer.append('-')

        # 만약 stack의 top이 seq의 front보다 크다면 수열을 만들수 없다.
        # 앞으로 stack에 push할 값은 seq의 front보다 크고, seq의 front보다 작은 값은 stack의 더 안쪽에 있기 때문에
        # 그 값을 빼올 방법이 없기 때문이다. 따라서 'NO'를 출력해야 한다.
        if stack and stack[-1] > seq[0]:
            answer.clear()
            answer.append('NO')
            break

    # nums가 비었다는 것은 이제 stack에 push할 것이 없다는 것을 의미한다.
    # 이는 이제 stack에서 pop밖에 하지 못하기 때문에 stack을 뒤집은 값들이 남은 수열의 값과 동일해야만 해당 수열을 만들 수 있다.
    # 그게 아니라면 'NO'를 출력해야 한다.
    else:
        stack.reverse()
        if stack == seq:
            for _ in range(len(seq)):
                answer.append('-')
        else:
            answer.clear()
            answer.append('NO')
        break

print(*answer, sep='\n')