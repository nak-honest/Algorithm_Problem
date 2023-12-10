sqr = [i**2 for i in range(1, int(50000 ** 0.5) + 1)]

def find_count(n):
    max_index = len(sqr) - 1

    for i in range(len(sqr)):
        if sqr[i] <= n:
            max_index = i

    if n == sqr[max_index]:
        return 1

    else:
        for i in range(max_index+1):
            if (n - sqr[i]) in sqr:
                return 2

    for i in range(max_index+1):
        for j in range(i, max_index+1):
            if (n - sqr[i] - sqr[j]) < 0:
                break
            elif (n - sqr[i] - sqr[j]) in sqr:
                return 3

    return 4


print(find_count(int(input())))

