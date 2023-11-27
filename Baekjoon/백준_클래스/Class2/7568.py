import sys


def is_larger(wh1, wh2):
    return wh1[0] > wh2[0] and wh1[1] > wh2[1]


N = int(input())
person = []
rank = [1] * N

for i in range(N):
    wh = list(map(int, sys.stdin.readline().split()))
    person.append([wh, i])

sorted_person = sorted(person, key=lambda x: (-x[0][0], -x[0][1]))

count = 0

for i in range(1, N):
    count = 0
    for j in range(i):
        if sorted_person[j][0][0] > sorted_person[i][0][0] and sorted_person[j][0][1] > sorted_person[i][0][1]:
            count += 1
    rank[sorted_person[i][1]] = count + 1

print(*rank)

'''
키, 덩치 순으로 정렬
(a, b) (b, c)

처음에는 등수를 전부 1로 설정한다.
앞에 있는 애는 뒤에 있는 애보다 키가 크거나 같다.
만약 같다면 두 아이의 등수는 같다.
만약 앞에가 더 크고, 몸무게도 크다면 다음 애는 앞의 애 + 1의 등수를 가진다.
만약 앞에가 더 크지만, 몸무게는 작거나 같다면 다음 애는 앞의 애의 등수를 그대로 가진다.

'''