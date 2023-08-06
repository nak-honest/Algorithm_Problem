import sys

N = int(input())
emo_log = set()
count = 0

for _ in range(N):
    chat = sys.stdin.readline().rstrip('\n')
    if chat == 'ENTER':
        emo_log.clear()
    elif chat not in emo_log:
        count += 1
        emo_log.add(chat)

print(count)