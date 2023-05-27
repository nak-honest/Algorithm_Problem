S = input()
sub_str = {}

for i in range(1, len(S) + 1):
    for j in range(0, len(S)):
        sub_str[S[j:j+i]] = 0

print(len(sub_str))