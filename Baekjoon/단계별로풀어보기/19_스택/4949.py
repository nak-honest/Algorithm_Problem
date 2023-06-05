cases = open(0).readlines()
cases.pop()

for sentence in cases:
    answer = 'yes'
    stack = []

    for c in sentence:
        if c in ['(', '[']:
            stack.append(c)
        elif c in [')', ']'] and not stack:
            answer = 'no'
            break
        elif (c == ')' and stack.pop() != '(') or (c == ']' and stack.pop() != '['):
            answer = 'no'
            break
    if stack:
        answer = 'no'

    print(answer)