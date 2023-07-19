import sys


def heappush(heap, item):
    heap.append(item)
    i = len(heap) - 1

    while i > 0:
        parent = (i - 1) // 2

        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break


def heappop(heap):
    n = len(heap)
    if n == 0:
        return 0

    heap[0], heap[n - 1] = heap[n - 1], heap[0]
    max_item = heap.pop()
    n -= 1
    i = 0

    while 2 * i + 1 < n:
        left = 2 * i + 1
        right = left + 1
        smaller = i

        if heap[left] < heap[smaller]:
            smaller = left
        if right < n and heap[right] < heap[smaller]:
            smaller = right

        if smaller == i:
            return max_item
        heap[i], heap[smaller] = heap[smaller], heap[i]
        i = smaller

    return max_item


N = int(input())
arr = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        print(heappop(arr))
    else:
        heappush(arr, x)