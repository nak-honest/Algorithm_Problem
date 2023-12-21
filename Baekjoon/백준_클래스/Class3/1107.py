# 걸린 시간 : 30분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

def get_channel_diff(n):
    if n == 0:
        return
    stack = [[]]

    while stack:
        channel = stack.pop()

        if len(channel) == n:
            global answer
            answer = min(answer, n + abs(int(''.join(channel)) - N))
            channel.pop()
            continue

        for next in button:
            stack.append(channel + [next])


N = int(input())
M = int(input())

not_button = []
if M != 0:
    not_button = list(map(int, input().split()))

button = [str(i) for i in range(10) if i not in not_button]
digits = len(str(N))

answer = abs(N - 100)

count = 0

chan = []

get_channel_diff(digits-1)
get_channel_diff(digits)
get_channel_diff(digits+1)

print(answer)