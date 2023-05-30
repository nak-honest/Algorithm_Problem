T, *nums = map(int, open(0).read().split())

i = 0
while i < len(nums):
    if nums[i] <= 3:
        print(max(nums[i], 2))
        i += 1
        continue

    # 루트 값 계산이 시간을 많이 잡아 먹는다. 이렇게 따로 빼놓아야 테스트를 통과한다.
    sqrt = int(nums[i]**0.5)

    for j in range(2, sqrt + 1):
        if nums[i] % j == 0:
            nums[i] += 1
            break
        elif j == sqrt:
            print(nums[i])
            i += 1
