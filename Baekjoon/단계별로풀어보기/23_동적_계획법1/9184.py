import sys

W = dict()

def get_W(a, b, c):
    if (a, b, c) in W:
        return W[(a, b, c)]
    if a <= 0 or b <= 0 or c <= 0:
        W[(a, b, c)] = 1
    elif a > 20 or b > 20 or c > 20:
        W[(a, b, c)] = get_W(20, 20, 20)
    elif a < b and b < c:
        W[(a, b, c)] = get_W(a, b, c-1) + get_W(a, b-1, c-1) - get_W(a, b-1, c)
    else:
        W[(a, b, c)] = get_W(a-1, b, c) + get_W(a-1, b-1, c) + get_W(a-1, b, c-1) - get_W(a-1, b-1, c-1)

    return W[(a, b, c)]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break

    print(f"w({a}, {b}, {c}) =", get_W(a, b, c))