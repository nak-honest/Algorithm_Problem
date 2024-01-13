# 걸린 시간 : 40분
# 제출 횟수 : 1번
# 풀이 참조 : x
# 반례 참조 : x

'''
!= 을 == 으로 잘못 적어서 계속 틀렸는데, 이걸 발견하는데 시간이 오래 걸렸다,,

홀수냐 짝수냐에 따라 달라진다.
1 2 3 2 1
1 2 2 1

일단 전체 수에서 모든 팰린드롬을 찾는다.
-> 팰린드롬에서 양쪽 끝 수를 하나씩 제거해도 팰린드롬이기 때문!

-> 먼저 팰린드롬이 가지고 있는 수의 개수가 짝수인 경우와 홀수인 경우로 나눈다.
-> 그 후 해당 팰린드롬의 가운데 수 정보와 전체 범위를 가지고 있는다.
-> 이를 dict로 저장한다. 팰린드롬이 s ~ e 의 수라면, Key는 s+e에 Value를 (s, e) 튜플을 저장한다.
-> 여기서 s+e는 원래 (s+e) / 2 로 가운데 수를 저장해야 하지만, 실수대신 정수를 저장하기 위해 s+e를 저장한다.

-> 그 후  S와 E가 주어지면 먼저 S+E 가 있는지를 확인한다.
-> 있다면 범위를 체크해서 범위를 벗어나지 않는지를 확인한다.
'''

import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
odd_palindrome = dict()
even_palindrome = dict()

# 짝수 개의 수를 가지는 팰린드롬을 찾는다.
for i in range(N-1):
    if nums[i] == nums[i+1]:
        s = i
        e = i+1
        while s-1 >= 0 and e+1 < N:
            if nums[s-1] != nums[e+1]:
                break
            s -= 1
            e += 1

        even_palindrome[s+e] = (s, e)

# 홀수 개의 수를 가지는 팰린드롬을 찾는다.
for i in range(N-2):
    if nums[i] == nums[i+2]:
        s = i
        e = i+2
        while s-1 >= 0 and e+1 < N:
            if nums[s-1] != nums[e+1]:
                break
            s -= 1
            e += 1

        odd_palindrome[s+e] = (s, e)

M = int(input())
answer = []

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    # 인덱스 조정
    S -= 1
    E -= 1

    # S와 E가 같은 경우는 숫자 한개인 경우이므로 언제나 팰린드롬이다.
    if S == E:
        answer.append(1)
        continue

    # S ~ E 의 가운데 수가 odd_palindrome에 있다면
    if (S + E) in odd_palindrome:
        min_s, max_e = odd_palindrome[S+E]
        # 범위 체크
        if S >= min_s and E <= max_e:
            answer.append(1)
            continue
    # S ~ E 의 가운데 수가 even_palindrome에 있다면
    if (S + E) in even_palindrome:
        min_s, max_e = even_palindrome[S+E]
        # 범위 체크
        if S >= min_s and E <= max_e:
            answer.append(1)
            continue

    answer.append(0)

print(*answer, sep='\n')