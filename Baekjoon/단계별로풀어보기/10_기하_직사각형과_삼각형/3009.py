cases = list(map(int, open(0).read().split()))
x_list = cases[::2]
y_list = cases[1::2]
answer = [0, 0]

for x, y in zip(x_list, y_list):
    if x_list.count(x) == 1:
        answer[0] = x
    if y_list.count(y) == 1:
        answer[1] = y

print(*answer)