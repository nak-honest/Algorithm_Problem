N = int(input())

answer = [' '*(N-i) + '*'*(2*i-1) for i in range(1, N+1)]

# 뒤에서 두번째 문자열부터 맨 앞 문자열까지 차례대로 extend
answer.extend(answer[-2::-1])

print(*answer, sep='\n')