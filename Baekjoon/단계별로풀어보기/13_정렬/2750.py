# sort() 함수 안쓰고 오랜만에 selection, insertion, bubble sort 를 직접 구현해봤다.
def selection_sort(num_list):
    sorted_list = num_list[:]
    for i in range(N):
        min_index = i
        for j in range(i + 1, N):
            if sorted_list[min_index] > sorted_list[j]:
                min_index = j

        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]

    return sorted_list


def insertion_sort(num_list):
    sorted_list = num_list[:]
    for i in range(1, N):
        for j in range(i, 0, -1):
            if sorted_list[j] < sorted_list[j-1]:
                sorted_list[j], sorted_list[j-1] = sorted_list[j-1], sorted_list[j]

    return sorted_list


def bubble_sort(num_list):
    sorted_list = num_list[:]
    for i in range(N-1, 0, -1):
        for j in range(i):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]

    return sorted_list


N, *num = map(int, open(0).read().split())
print(*selection_sort(num))
# print(*insertion_sort(num))
# print(*bubble_sort(num))
