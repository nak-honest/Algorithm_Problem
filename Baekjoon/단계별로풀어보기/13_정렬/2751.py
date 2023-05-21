# sort() 함수를 사용하지 않고 직접 merge, quick, heap sort를 구현해보겠다.
# 단 quick sort는 최악의 경우 O(N^2)이므로 테스트에 통과하지는 못한다.
def merge_sort(unsorted_list):
    merge_sort_recursive(unsorted_list, 0, len(unsorted_list) - 1)


def merge_sort_recursive(unsorted_list, left, right):
    if left < right:
        merge_sort_recursive(unsorted_list, left, (left + right) // 2)
        merge_sort_recursive(unsorted_list, (left + right) // 2 + 1, right)
        merge(unsorted_list, left, right)


def merge(unsorted_list, left, right):
    copied_list = unsorted_list[left:right+1]
    index = 0
    i = left
    j = (left + right) // 2 + 1
    while i <= (left + right) // 2 and j <= right:
        if unsorted_list[i] >= unsorted_list[j]:
            copied_list[index] = unsorted_list[j]
            j += 1
        else:
            copied_list[index] = unsorted_list[i]
            i += 1
        index += 1

    if i > right:
        while j <= right:
            copied_list[index] = unsorted_list[j]
            j += 1
            index += 1
    else:
        while i <= (left + right) // 2:
            copied_list[index] = unsorted_list[i]
            i += 1
            index += 1

    unsorted_list[left:right+1] = copied_list


def quick_sort(unsorted_list):
    quick_sort_recursive(unsorted_list, 0, len(unsorted_list)-1)


def quick_sort_recursive(unsorted_list, left, right):
    if right > left:
        pivot = left
        pivot_item = unsorted_list[left]
        for i in range(left + 1, right + 1):
            if pivot_item > unsorted_list[i]:
                unsorted_list[pivot+1], unsorted_list[i] = unsorted_list[i], unsorted_list[pivot+1]
                pivot += 1
        unsorted_list[left], unsorted_list[pivot] = unsorted_list[pivot], unsorted_list[left]
        quick_sort_recursive(unsorted_list, left, pivot-1)
        quick_sort_recursive(unsorted_list, pivot + 1, right)


def make_heap(my_list):
    heap = my_list[:]
    for i in range(len(heap) // 2 - 1, -1, -1):
        parent_index = i

        while parent_index <= len(heap) // 2 - 1:
            left_index = (parent_index + 1) * 2 - 1
            right_index = (parent_index + 1) * 2
            smallest_index = left_index
            if right_index < len(heap) and heap[right_index] < heap[smallest_index]:
                smallest_index = right_index

            if heap[parent_index] > heap[smallest_index]:
                heap[parent_index], heap[smallest_index] = heap[smallest_index], heap[parent_index]
                parent_index = smallest_index
            else:
                break
    return heap


def remove_min(heap):
    min_item = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    parent_index = 0
    while parent_index <= len(heap) // 2 - 1:
        left_index = (parent_index + 1) * 2 - 1
        right_index = (parent_index + 1) * 2
        smallest_index = left_index
        if right_index < len(heap) and heap[right_index] < heap[smallest_index]:
            smallest_index = right_index

        if heap[parent_index] > heap[smallest_index]:
            heap[parent_index], heap[smallest_index] = heap[smallest_index], heap[parent_index]
            parent_index = smallest_index
        else:
            break

    return min_item


def heap_sort(unsorted_list):
    heap = make_heap(unsorted_list)
    for i in range(len(unsorted_list)):
        unsorted_list[i] = remove_min(heap)


N, *nums = map(int, open(0).read().split())


merge_sort(nums)
# quick_sort(nums)
# heap_sort(nums)
print(*nums, sep='\n')
