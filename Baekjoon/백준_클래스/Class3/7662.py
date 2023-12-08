import sys
from heapq import heappop
from heapq import heappush

for _ in range(int(input())):
    k = int(input())
    max_heap = []
    min_heap = []
    # 해당 수가 현재 몇개 있는지를 저장한다.
    num_dict = dict()

    for _ in range(k):
        commands = sys.stdin.readline().split()

        if commands[0] == 'I':
            num = int(commands[1])
            heappush(min_heap, num)
            heappush(max_heap, -num)
            num_dict[num] = num_dict.get(num, 0) + 1
        elif commands[1] == '1':
            # max_heap에서 최대값을 제거한다. min_heap에서 해당 수를 다 삭제한 경우에는, 다음 최대값을 삭제한다.
            while max_heap:
                max_num = -heappop(max_heap)
                if num_dict[max_num] > 0:
                    num_dict[max_num] -= 1
                    break
        else:
            # min_heap에서 최소값을 제거한다. max_heap에서 해당 수를 다 삭제한 경우에는, 다음 최소값을 삭제한다.
            while min_heap:
                min_num = heappop(min_heap)
                if num_dict[min_num] > 0:
                    num_dict[min_num] -= 1
                    break

    answer = []
    # 위의 방식과 똑같이 최대값을 찾는다.
    while max_heap:
        max_num = -heappop(max_heap)
        if num_dict[max_num] > 0:
            answer.append(max_num)
            break

    # 위의 방식과 똑같이 최소값을 찾는다.
    while min_heap:
        min_num = heappop(min_heap)
        if num_dict[min_num] > 0:
            answer.append(min_num)
            break

    if answer:
        print(*answer)
    else:
        print("EMPTY")
