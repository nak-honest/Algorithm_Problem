words = [input() for _ in range(5)]

max_len = len(max(words, key=len))

# 각 단어 뒤에 공백을 붙여서 모든 단어의 크기를 통일시킨다.
words = [w + ' ' * (max_len - len(w)) for w in words]

answer = ''
for j in range(max_len):
    for i in range(5):
        answer += words[i][j]

# 앞에서 붙인 공백을 없애서 출력한다.
print(answer.replace(' ', ''))


