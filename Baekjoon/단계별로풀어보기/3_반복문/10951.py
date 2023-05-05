operands = list(map(int, open(0).read().split()))
n = len(operands)//2

answer = [operands[2*i] + operands[2*i+1] for i in range(n)]
print(*answer, sep='\n')