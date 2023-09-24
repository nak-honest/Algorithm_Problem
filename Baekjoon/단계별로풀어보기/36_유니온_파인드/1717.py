# 걸린 시간 : 10분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

# 크루스칼 알고리즘에 의해 이미 익숙한 유니온 파인드 기본문제. 그냥 코드를 보면 바로 이해할 수 있다.
import sys

def find_root(i):
    while union_set[i] != i:
        i = union_set[i]

    return i

n, m = map(int, sys.stdin.readline().split())
union_set = [i for i in range(n+1)]
depth = [0 for _ in range(n+1)]

is_same_set = ["NO", "YES"]

for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())
    root_of_a = find_root(a)
    root_of_b = find_root(b)

    # depth가 무한정으로 깊어지지 않도록 하기 위해 depth가 늘지 않는다면 늘지 않는쪽으로 합친다.
    if command == 0 and root_of_a != root_of_b:
        if depth[root_of_a] > depth[root_of_b]:
            union_set[root_of_b] = root_of_a
        elif depth[root_of_a] < depth[root_of_b]:
            union_set[root_of_a] = root_of_b
        else:
            union_set[root_of_b] = root_of_a
            depth[root_of_a] += 1
    elif command == 1:
        print(is_same_set[int(root_of_a == root_of_b)])
