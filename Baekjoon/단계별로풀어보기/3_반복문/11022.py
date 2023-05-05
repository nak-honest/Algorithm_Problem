n, *op = map(int, open(0).read().split())
answer = ["Case #" + str(i+1) + ": " + str(op[2*i]) + " + " + str(op[2*i+1]) + " = " + str(op[2*i]+op[2*i+1])
          for i in range(n)]
print(*answer, sep='\n')