# '-' 뒤의 수가 클수록 전체 결과는 작아진다.
# 따라서 '-'를 기준으로 문자열을 나누고 맨 앞을 제외한 나머지 부분들은 모두 빼주면 된다.

expression = input().split('-')

subtrahend = []

for poly in expression:
    sum_of_poly = sum(map(int, poly.split('+')))
    subtrahend.append(sum_of_poly)


answer = subtrahend[0]
for i in range(1, len(subtrahend)):
    answer -= subtrahend[i]

print(answer)