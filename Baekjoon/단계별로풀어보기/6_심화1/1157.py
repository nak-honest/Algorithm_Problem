from collections import Counter
c = Counter(input().upper()).most_common()

# 알파벳 하나로만 이루어져 있거나 가장 많이 사용된 알파벳이 하나인 경우
if len(c) == 1 or c[0][1] != c[1][1]:
    print(c[0][0])
# 가장 많이 사용된 알파벳이 여러개인 경우
else:
    print('?')