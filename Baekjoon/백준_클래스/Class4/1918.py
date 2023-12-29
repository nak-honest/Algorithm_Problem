# 걸린 시간 : 1시간
# 제출 횟수 : 2번
# 풀이 참조 : x
# 반례 참조 : x

mid = input()

answer = []
operations = []

for c in mid:
    if c == '(':
        operations.append(c)
    elif c == ')':
        while operations:
            if operations[-1] == '(':
                operations.pop()
                break

            answer.append(operations.pop())

        while operations and (operations[-1] == '*' or operations[-1] == '/'):
            answer.append(operations.pop())
    elif c == '*' or c == '/':
        if operations and (operations[-1] == '*' or operations[-1] == '/'):
            answer.append(operations.pop())
        operations.append(c)
    elif c == '+' or c == '-':
        if not operations or operations[-1] == '(':
            operations.append(c)
        else:
            while operations and operations[-1] != '(':
                answer.append(operations.pop())
            operations.append(c)
    else:
        answer.append(c)

while operations:
    answer.append(operations.pop())

print(''.join(answer))



'''
문자인 경우 바로 놓는다.
여는 괄호인 경우 연산자 스택에 바로 넣는다.
닫는 괄호인 연산자 스택에서 여는 괄호가 나올때까지 뺀다. 그리고 그 뒤에 있는 *,/ 까지만 뺀다.
*, / 인 경우, 연산자 스택 맨 위가 *, / 라면 뺀다. 그 후 연산자 스택에 추가한다.
+, - 인 경우 연산자 스택이 비어있거나 가장 위가 여는 괄호라면 스택에 추가한다.
+, - 인 경우 연산자 스택의 위가 연산자라면 여는 괄호가 나올때까지 뺀다.
'''