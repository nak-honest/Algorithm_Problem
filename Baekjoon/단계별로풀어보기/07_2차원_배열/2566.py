nums = list(map(int, open(0).read().split()))

max_num = max(nums)
index = nums.index(max_num)

print(max_num)
print(index//9 + 1, index%9 + 1)
