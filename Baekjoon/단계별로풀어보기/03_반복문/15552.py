n, *op = map(int, open(0).read().split())
print(*[op[2*i]+op[2*i+1] for i in range(n)], sep='\n')