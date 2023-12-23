def get_seq(seq):
    if len(seq) == M:
        seqs.add(tuple(seq))
        return

    for i in range(N):
        if not visited[i]:
            seq.append(nums[i])
            visited[i] = True
            get_seq(seq)
            seq.pop()
            visited[i] = False


N, M = map(int, input().split())
nums = list(map(int, input().split()))

visited = [False] * N
seqs = set()

if M == 1:
    print(*sorted(set(nums)), sep='\n')
else:
    get_seq([])
    for seq in sorted(seqs):
        print(*list(seq))