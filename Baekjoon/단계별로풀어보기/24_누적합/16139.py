import sys

S = input()
q = int(input())
alphabet_count = [[0 for _ in range(26)]]


for i in range(len(S)):
    alphabet_count[i][ord(S[i])-97] += 1
    alphabet_count.append(alphabet_count[-1][:])


for _ in range(q):
    a, l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)

    i = ord(a) - 97

    answer = alphabet_count[r][i] - alphabet_count[l][i] + 1
    if alphabet_count[l][i] == 0 or (l != 0 and alphabet_count[l][i] == alphabet_count[l - 1][i]):
        answer -= 1

    print(answer)



