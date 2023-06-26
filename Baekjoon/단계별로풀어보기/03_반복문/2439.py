n = int(input())
answer = [" "*(n-i) + "*"*i for i in range(1, n+1)]

print(*answer, sep='\n')