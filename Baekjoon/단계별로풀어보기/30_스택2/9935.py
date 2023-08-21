s = input().rstrip('\n')
bomb = input().rstrip('\n')

# 터질수 있는 폭탄을 담을 스택
bomb_candidate = []
answer = []

# 스택에 넣을때마다 인덱스를 업데이트한다.
index = 0

for c in s:
    # 폭탄의 마지막 문자가 스택에 들어가는 경우 폭발한다.
    if index == len(bomb) - 1 and c == bomb[index]:
        # 폭발하기 때문에 bomb_candidate에서 폭탄을 없앤다.
        for _ in range(len(bomb) - 1):
            bomb_candidate.pop()
        # bomb_candidate에 여전히 폭발이 될수 있는 문자들이 남은 경우, 스택의 마지막 인덱스 + 1을 index로 삼는다.
        if bomb_candidate:
            index = bomb_candidate[-1][1] + 1
        # bomb_candidate가 비어있는 경우 index를 0으로 삼는다.
        else:
            index = 0
    # 현재 index에 맞는 폭탄의 문자가 들어온 경우 bomb_candidate에 넣는다.
    elif c == bomb[index]:
        bomb_candidate.append((c, index))
        index += 1
    # 만약 c가 현재 index에 맞는 폭탄의 문자는 아니지만 폭탄의 첫번째 문자라면 이 문자로 시작하는 폭탄이 폭발한 후, 앞의 폭탄 후보가 터질 수도 있다.
    # 따라서 스택에 넣고 다시 index를 1로 삼는다.
    elif c == bomb[0]:
        bomb_candidate.append((c, 0))
        index = 1
    # 만약 c가 폭발이 불가능한 문자라면 bomb_candidate에 있는 모든 내용을 answer에 집어넣고 clear 한다.
    # index는 다시 0으로 초기화한다.
    elif bomb_candidate:
        for candidate in bomb_candidate:
            answer.append(candidate[0])
        bomb_candidate.clear()
        index = 0
        answer.append(c)
    # 만약 bomb_candidate가 비어있고 c가 폭탄의 첫번째 문자가 아니라면 그냥 answer에 추가한다.
    else:
        answer.append(c)

# bomb_candidate에 남아있는 모든 문자를 answer에 추가한다.
for c, index in bomb_candidate:
    answer.append(c)

if answer:
    print(''.join(answer))
else:
    print("FRULA")