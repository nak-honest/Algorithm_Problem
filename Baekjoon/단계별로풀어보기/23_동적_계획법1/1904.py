N = int(input())
seq_num = [0, 1, 2] + [0]*(N-2)

for i in range(3, N+1):
    seq_num[i] = seq_num[i-1] + seq_num[i-2]
    if seq_num[i] >= 15746:
        seq_num[i] -= 15746

print(seq_num[N])

