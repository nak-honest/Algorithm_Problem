# 걸린 시간 : 15분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

parent = dict()

for _ in range(int(input())):
    proposition = input()
    p = proposition[-1]
    c = proposition[0]
    parent[c] = p

    if p not in parent:
        parent[p] = -1

for _ in range(int(input())):
    proposition = input()
    c = proposition[0]
    p = parent[c]
    answer = 'F'

    while p != -1:
        if p == proposition[-1]:
            answer = 'T'
            break
        p = parent[p]

    print(answer)
