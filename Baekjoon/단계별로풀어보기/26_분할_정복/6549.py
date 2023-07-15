# 처음에 분할 정복으로 풀다가 시간초과로 실패했다.
# 그러다 heap으로 접근하니 어렵지 않게 풀수 있었다.
# 1725 문제와 완전히 동일하다.

import sys
from heapq import heappop, heappush

while True:
    tc = sys.stdin.readline().split()
    if tc[0] == '0':
        break

    n, *h = map(int, tc)

    # heap은 max_heap으로 높이가 클수록 우선순위가 높다.
    # heap에는 높이와 인덱스를 같이 저장시킨다.
    heap = [[-h[0], 0]]

    # len_of_h[i]는 index i에서 h[i]의 높이로 만들수 있는 직사각형의 최대 길이(width)가 저장된다.
    len_of_h = [0 for _ in range(n)]

    # 왼쪽에서부터 오른쪽으로 탐색하면서 len_of_h를 업데이트한다.
    # heap에는 오른쪽으로 진행하면서 직사각형의 넓이를 넓힐수 있는 인덱스만 들어있다.
    for i in range(1, len(h)):
        # h[i]가 heap[0]보다 작다면 heap[0]에 있는 높이로는 더이상 오른쪽으로 직사각형의 넓이를 넓힐 수 없다.
        # 따라서 len_of_h를 업데이트하고, heap에서 pop한다.
        while heap and -heap[0][0] > h[i]:
            len_of_h[heap[0][1]] = i - heap[0][1]
            heappop(heap)

        heappush(heap, [-h[i], i])

    # heap에 남아있다는 것은 오른쪽 끝까지 직사각형의 넓이를 넓힐수 있다는 것이다.
    while heap:
        len_of_h[heap[0][1]] = n - heap[0][1]
        heappop(heap)

    # 이번에는 오른쪽에서 왼쪽으로 탐색하면서 len_of_h를 업데이트 한다.
    heap.append([-h[n - 1], n - 1])

    # heap에는 왼쪽으로 진행하면서 직사각형의 넓이를 넓힐수 있는 인덱스만 들어있다.
    for i in range(n - 2, -1, -1):
        # h[i]가 heap[0]보다 작다면 heap[0]에 있는 높이로는 더이상 왼쪽으로 직사각형의 넓이를 넓힐 수 없다.
        # 따라서 len_of_h를 업데이트하고, heap에서 pop한다.
        while heap and -heap[0][0] > h[i]:
            len_of_h[heap[0][1]] += (heap[0][1] - i - 1)
            heappop(heap)

        heappush(heap, [-h[i], i])

    # heap에 남아있다는 것은 왼쪽 끝까지 직사각형의 넓이를 넓힐수 있다는 것이다.
    while heap:
        len_of_h[heap[0][1]] += heap[0][1]
        heappop(heap)

    # 각 인덱스에서 h[i]의 높이로 만들수 있는 직사각형의 최대 넓이를 계산 한다.
    area = [h[i] * len_of_h[i] for i in range(n)]

    # 그 중 최대값을 반환한다.
    print(max(area))

'''
# 밑의 코드는 나쁘지 않은 접근이었지만, 지그재그 형식으로 직사각형이 이루어져 있으면 시간초과가 발생한다.

import sys
from heapq import heappop, heappush

sys.setrecursionlimit(10000)

max_area = 0

# arr의 최대값이 저장되어 있는 인덱스를 저장시킨다.
def find_max_index(arr, i, j):
    max_index = i
    max_val = 0
    for index in range(i, j):
        if arr[index] > max_val:
            max_index = index
            max_val = arr[index]

    return max_index


# h_arr[i:j]에서 가장 큰 직사각형을 찾는다.
def get_max_area(h_arr, i, j, len_of_h):
    global max_area
    max_index = find_max_index(h_arr, i, j)
    max_h = h_arr[max_index]

    left = max_index - 1
    right = max_index + 1

    # 왼쪽과 오른쪽으로 퍼지면서 가장 큰 직사각형을 찾는다.
    # 이때 왼쪽과 오른쪽으로 퍼질때 직사각형의 높이가 더 커진다면 멈춘다.
    # 이는 max_h 가 계속 감소되면서 h[i:j]에서 max_h의 높이를 가진 직사각형을 탐색하기 때문이다.
    # 만약 양쪽으로 퍼지다 더 높이가 큰 직사각형이 존재하게되면 max_h의 높이를 가지는 직사각형을 만들수 없게 된다.
    # 따라서 그러한 부분은 왼쪽, 오른쪽 영역으로 나누어서 해당 영역에 대해 다시 재귀적으로 큰 직사각형을 찾는다.
    while (left >= i and h_arr[left+1] >= h_arr[left]) or (right < j and h_arr[right-1] >= h_arr[right]):
        while left >= i and h_arr[left] == max_h:
            left -= 1
        while right < j and h_arr[right] == max_h:
            right += 1

        max_area = max(max_area, max_h * (right - left - 1))

        if left >= i and right < j:
            # 왼쪽, 오른쪽 영역이 아직 남은 경우
            if max(h_arr[left], h_arr[right]) > max_h:
                max_h = min(max_h, h_arr[left], h_arr[right])
            else:
                max_h = min(max_h, max(h_arr[left], h_arr[right]))
        elif left >= i:
            # 왼쪽 영역만 남은 경우
            max_h = min(max_h, h_arr[left])
        elif right < j:
            # 오른쪽 영역만 남은 경우
            max_h = min(max_h, h_arr[right])

    # 왼쪽, 오른쪽 영역을 뒤질수 있는 영역까지 다 뒤졌다면 재귀적으로 남은 왼쪽 영역과 오른쪽 영역에 대해 최대 사각형을 찾는다.
    if left >= i:
        get_max_area(h_arr, i, left + 1, len_of_h)
    if right < j:
        get_max_area(h_arr, right, j, len_of_h)

    max_area = max(max_area, h_arr[left+1] * len_of_h[left+1])
    max_area = max(max_area, h_arr[right-1] * len_of_h[right-1])


while True:
    max_area = 0
    tc = sys.stdin.readline().split()
    if tc[0] == '0':
        break

    n, *h = map(int, tc)


    heap = [[-h[0], 0]]
    len_of_h = [0 for _ in range(n)] # len_of_h[i]는 index i에서 h[i]의 높이로 만들수 있는 직사각형의 넓이가 저장된다.

    for i in range(1, len(h)):
        while heap and -heap[0][0] > h[i]:
            len_of_h[heap[0][1]] = i - heap[0][1]
            heappop(heap)

        heappush(heap, [-h[i], i])

    while heap:
        len_of_h[heap[0][1]] = n - heap[0][1]
        heappop(heap)

    heap.append([-h[n-1], n-1])

    for i in range(n-2, -1, -1):
        while heap and -heap[0][0] > h[i]:
            len_of_h[heap[0][1]] += (heap[0][1] - i - 1)
            heappop(heap)

        heappush(heap, [-h[i], i])

    while heap:
        len_of_h[heap[0][1]] += heap[0][1]
        heappop(heap)


    get_max_area(h, 0, n, len_of_h)
    print(max_area)
'''