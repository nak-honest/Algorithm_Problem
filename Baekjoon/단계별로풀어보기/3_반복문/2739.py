x = int(input())
answer = [str(x) + " * " + str(i) + " = " + str(x*i) for i in range(1, 10)]
print(*answer, sep='\n')