from functools import reduce
print(reduce(lambda x, y: x*y, [1] + [i for i in range(1, int(input())+1)]))