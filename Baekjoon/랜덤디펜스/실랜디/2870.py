# 걸린 시간 : 15분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

N = int(input())

answer = []

for _ in range(N):
    string = input().rstrip('\n')
    start = 0

    while start < len(string):
        if string[start].isdigit():
            end = start
            while end < len(string) and string[end].isdigit():
                end += 1

            answer.append(int(string[start:end]))
            start = end

        start += 1

print(*sorted(answer), sep='\n')
