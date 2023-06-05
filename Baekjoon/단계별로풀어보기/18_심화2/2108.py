import sys
from collections import Counter

N = int(input())
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()

count = Counter(nums).most_common()
most = count[0][0]

if N > 1 and count[0][1] == count[1][1]:
    most = sorted(filter(lambda x: x[1] == count[0][1], count))[1][0]


print(round(sum(nums) / N), nums[(N-1)//2], most, nums[-1] - nums[0], sep='\n')