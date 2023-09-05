import sys

n = int(input())
seq = sorted(map(int, sys.stdin.readline().split()))
x = int(input())

count = 0
i = 0
j = n-1

# 투포인터로 양쪽 끝에서 줄여가며 그 합을 확인한다.
while i < n and j > i:
    sum_of_pairs = seq[i] + seq[j]
    if sum_of_pairs == x:
        count += 1
        i += 1
    elif sum_of_pairs > x:
        j -= 1
    else:
        i += 1

print(count)