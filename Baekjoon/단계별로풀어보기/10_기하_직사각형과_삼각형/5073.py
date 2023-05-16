sides = list(map(int, open(0).read().split()))
cases = [sides[i:i+3] for i in range(0, len(sides) - 3, 3)]
answer = ['Invalid', 'Equilateral', 'Isosceles', 'Scalene']

for c in cases:
    condition = [max(c) >= sum(c) - max(c), len(set(c)) == 1, len(set(c)) == 2, len(set(c)) == 3]
    index = list(filter(lambda i: condition[i], range(4)))
    print(answer[index[0]])