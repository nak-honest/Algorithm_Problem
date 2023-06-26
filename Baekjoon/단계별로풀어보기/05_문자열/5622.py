# A-Z의 ASCII code 저장
alphas = [i for i in range(65, 91)]

# index slicing을 위해 범위를 저장한다. ABC -> 0~2, DEF -> 3~5, ...
index = [0, 3, 6, 9, 12, 15, 19, 22, 26]

# {A: 3, B: 3, C: 3, ..., Y: 10, Z: 10}
alpha_time = {chr(alpha): i+3 for i in range(len(index)-1) for alpha in alphas[index[i]:index[i+1]]}

print(sum([alpha_time[c] for c in input()]))
