num = list(map(int, open(0).read().split()))

max_num = max(num)
print(max_num, num.index(max_num)+1, sep='\n')