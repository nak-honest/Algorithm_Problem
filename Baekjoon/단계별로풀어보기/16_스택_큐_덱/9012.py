T = int(input())

for _ in range(T):
    ps = input()
    stack = []
    answer = 'YES'

    for c in ps:
        if c == '(':
            stack.append(c)
        elif stack:
            stack.pop()
        else:
            answer = 'NO'

    if stack:
        answer = 'NO'

    print(answer)
