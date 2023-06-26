from functools import reduce
N = int(input())
print(reduce(lambda x, y: x*y-1, [2]*(N+1))**2)

# print((2**N + 1) ** 2)
