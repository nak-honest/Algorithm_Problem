from itertools import dropwhile

N, *num = map(int, open(0).read().split())
count = 0

for n in num:
    # 2부터 n-1까지 모두 나눌때의 나머지가 0이 아닌지를 본다.
    # 만약 모두 나머지가 0이 아니면(소수라면) dropwhile은 길이가 0이 된다.
    if n != 1 and not list(dropwhile(lambda i: n % i != 0, range(2, n))):
        count += 1

print(count)
