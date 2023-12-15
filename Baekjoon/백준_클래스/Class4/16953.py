import sys
answer = sys.maxsize

count = 0
def find(a, b):
    global count

    if a == b:
        global answer
        answer = min(answer, count)
    elif a < b:
        count += 1
        find(a*2, b)
        find(a*10 + 1, b)
        count -= 1

A, B = map(int, input().split())
find(A, B)

if answer == sys.maxsize:
    print(-1)
else:
    print(answer + 1)
