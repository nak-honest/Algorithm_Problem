# Meet In The Middle 알고리즘을 처음 알았다.
# 혼자서는 풀지 못했다.

# left와 right의 원소 합이 C보다 작거나 같은 경우의 수를 모두 구한다.
# 자세한 내용은 뒤의 내용을 확인한 뒤 함수 내용을 보면 더 잘 이해가 될 것이다.
def get_count(l, r):
    j = len(right) - 1

    count = 0

    # 투 포인터를 이용해서 left와 right의 원소합이 C보다 작은 경우의 수를 구한다.
    # 이분탐색을 이용해서 풀어도 된다.
    for i in range(len(left)):
        while l[i] + r[j] > C:
            j -= 1

            if j == -1:
                return count

        count += (j + 1)

    return count


N, C = map(int, input().split())
items = list(map(int, input().split()))

# mid를 기준으로 아이템들을 두개의 집합으로 쪼갠다.
mid = len(items) // 2

left = []
right = []

# 부분집합을 위한 비트마스크
bit_mask = 0

# mid를 기준으로 왼쪽 집합의 모든 부분집합의 원소 합을 left에 추가한다.
while bit_mask < (1 << mid):
    sub_sum = 0

    for i in range(mid):
        if (bit_mask & (1 << i)) != 0:
            sub_sum += items[i]

    left.append(sub_sum)
    bit_mask += 1


bit_mask = 0

# mid를 기준으로 오른쪽 집합의 모든 부분집합의 원소 합을 right에 추가한다.
while bit_mask < (1 << (len(items) - mid)):
    sub_sum = 0

    for i in range(len(items) - mid):
        if (bit_mask & (1 << i)) != 0:
            sub_sum += items[mid + i]

    right.append(sub_sum)
    bit_mask += 1

# left와 right를 sort시킨후 left와 right에서 하나씩 값을 가지고 와서 더했을때
# 그 값이 C를 넘지 않는다면 가방에 넣는 경우의 수 중 하나이다.
# 왜냐하면 left와 right의 원소는 부분집합의 합을 의미하는데, 두 부분집합의 합을 더한 값이 C보다 작거나 같다는 것은,
# 각각의 부분집합을 이루는 원소들로 가방을 채웠을때 그 무게가 C보다 작거나 같은 것을 의미하기 때문이다.
left.sort()
right.sort()

print(get_count(left, right))
