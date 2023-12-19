import sys

N = int(input())
M = int(input())

S = sys.stdin.readline().rstrip('\n')
is_cur_counting = False

answer = 0
count = 0

for i in range(len(S)):
    if not is_cur_counting and S[i] == 'I':
        is_cur_counting = True
    elif is_cur_counting:
        if S[i-1] == S[i]:
            count = 0
            if S[i] == 'O':
                is_cur_counting = False
        elif S[i-1] == 'O' and S[i] == 'I':
            count += 1
            if count >= N:
                answer += 1

print(answer)
