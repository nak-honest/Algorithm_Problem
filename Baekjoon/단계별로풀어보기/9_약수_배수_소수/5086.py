cases = list(map(int, open(0).read().split()))

cases.pop()
cases.pop()

for i in range(len(cases)//2):
    a = cases[2*i]
    b = cases[2*i+1]

    if b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')