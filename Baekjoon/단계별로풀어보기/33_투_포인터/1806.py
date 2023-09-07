import sys

N, S = map(int, input().split())
seq = list(map(int, sys.stdin.readline().split()))

i = 0 # 부분합의 가장 왼쪽 인덱스를 가리키는 포인터
j = 0 # 부분합의 가장 오른쪽 인덱스를 가리키는 포인터

min_len = sys.maxsize

sub_sum = seq[i]

# 투포인터로 부분합이 S가 넘는 경우의 길이를 구한다.
while True:
    if sub_sum >= S:
        min_len = min(min_len, j - i + 1)

        # sub_sum이 S보다 크거나 같은 경우 부분합이 작아져야 한다.
        # 따라서 i를 1 증가시킨다.
        # 하지만 현재 j와 i가 같은 경우 i는 더이상 증가시킬수 없기 때문에 j를 먼저 증가시킨다.
        if i + 1 <= j:
            sub_sum -= seq[i]
            i += 1
        else:
            j += 1

            if j == N:
                break

            sub_sum += seq[j]

    # 부분합이 S보다 작다면 j를 1 증가시킨다.
    else:
        j += 1

        if j == N:
            break

        sub_sum += seq[j]

if min_len == sys.maxsize:
    min_len = 0
print(min_len)