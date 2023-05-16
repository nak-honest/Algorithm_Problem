N, *cases = map(int, open(0).read().split())
x_list = cases[::2]
y_list = cases[1::2]

answer = (max(x_list) - min(x_list)) * (max(y_list) - min(y_list))
print(answer)