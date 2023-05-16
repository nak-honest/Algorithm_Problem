angles = list(map(int, open(0).read().split()))
answer = ['Error', 'Equilateral', 'Isosceles', 'Scalene']
condition = [sum(angles) != 180, len(set(angles)) == 1, len(set(angles)) == 2, len(set(angles)) == 3]
index = list(filter(lambda i: condition[i], range(4)))

print(answer[index[0]])
