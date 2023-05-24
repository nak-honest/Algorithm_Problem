N, *X_list = map(int, open(0).read().split())

X_set = set(X_list)
sorted_X_without_duplication = sorted(X_set)
X_dict = {}
for i in range(len(sorted_X_without_duplication)):
    X_dict[sorted_X_without_duplication[i]] = i

answer = [X_dict[X] for X in X_list]
print(*answer)