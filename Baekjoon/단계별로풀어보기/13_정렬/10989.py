# 메모리 효율 문제인데, 생각보다 잘 안 풀렸다. 계속 메모리 초과가 발생했다..
# 카운팅 정렬에 대해서도 처음 알게 되었다.
import sys

N = int(input())
nums = [0 for _ in range(10001)]

for _ in range(N):
    nums[int(sys.stdin.readline().rstrip('\n'))] += 1

index = 0
for count in nums:
    if count != 0:
        for _ in range(count):
            print(index)
    index += 1
