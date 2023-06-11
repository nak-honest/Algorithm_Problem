# 문제 푸는데 한시간정도 걸렸다.. 어려웠다..
# 특히 세제곱근을 구할때 int(N ** (1 / 3))으로 구했는데, 이렇게 하면 제대로 된 값이 나오지 않는다.
def get_star(n):
    if n == 1:
        return pattern
    else:
        prev = get_star(n-1)
        return [p*3 for p in prev] + [p + " "*(3**(n-1)) + p for p in prev] + [p*3 for p in prev]


pattern = [
    "***",
    "* *",
    "***"
]

N = int(input())
k = 0
while N > 1:
    N = N//3
    k += 1

print('\n'.join(get_star(k)))
