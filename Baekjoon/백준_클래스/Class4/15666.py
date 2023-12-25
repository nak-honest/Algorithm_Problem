def get_seq(seq):
    if len(seq) == M:
        seqs.add(tuple(seq))
        return

    for num in nums:
        if not seq or num >= seq[-1]:
            seq.append(num)
            get_seq(seq)
            seq.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))

seqs = set()
if M == 1:
    print(*sorted(set(nums)))
else:
    get_seq([])
    for seq in sorted(seqs):
        print(*list(seq))
