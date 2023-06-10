# 문제에서 주어진 의사코드를 그대로 구현하니 조금 더 복잡해 보이긴 한다.
# 하지만 merge sort 자체는 수차례 구현해 봤기 때문에 그냥 의사코드 그대로 푼다.

def merge_sort(A, p, r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    global cnt

    if cnt >= k:
        return

    tmp = A[p:r+1]
    i = p
    j = q + 1
    t = 0

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            t += 1
            i += 1
        else:
            tmp[t] = A[j]
            t += 1
            j += 1

        cnt += 1
        if cnt == k:
            print(tmp[t-1])

    while i <= q:
        tmp[t] = A[i]
        t += 1
        i += 1

        cnt += 1
        if cnt == k:
            print(tmp[t-1])
    while j <= r:
        tmp[t] = A[j]
        t += 1
        j += 1

        cnt += 1
        if cnt == k:
            print(tmp[t-1])

    A[p:r+1] = tmp


global cnt
cnt = 0
n, k = map(int, input().split())
arr = list(map(int, input().split()))

merge_sort(arr, 0, len(arr) - 1)

if cnt < k:
    print(-1)