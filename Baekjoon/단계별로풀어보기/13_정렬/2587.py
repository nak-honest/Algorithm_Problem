num = list(map(int, open(0).read().split()))
print(sum(num) // len(num), sorted(num)[2], sep='\n')