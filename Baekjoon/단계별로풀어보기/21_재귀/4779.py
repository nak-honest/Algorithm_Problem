def cantor(s_list):
    cantor_rec(s_list, 0, len(s_list)-1)


def cantor_rec(s_list, left, right):
    if left < right:
        interval = (right - left + 1) // 3
        s_list[left+interval:right-interval+1] = [' '] * interval
        cantor_rec(s_list, left, left+interval-1)
        cantor_rec(s_list, right-interval+1, right)


nums = list(map(int, open(0).read().split()))

for N in nums:
    answer = ['-'] * (3**N)
    cantor(answer)
    print(''.join(answer))