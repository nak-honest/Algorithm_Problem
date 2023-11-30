import sys

M = int(input())
S = set()

for _ in range(M):
    commands = sys.stdin.readline().split()
    if commands[0] == "add":
        S.add(int(commands[1]))
    elif commands[0] == "remove" and int(commands[1]) in S:
        S.remove(int(commands[1]))
    elif commands[0] == "check":
        if int(commands[1]) in S:
            print(1)
        else:
            print(0)
    elif commands[0] == "toggle":
        if int(commands[1]) in S:
            S.remove(int(commands[1]))
        else:
            S.add(int(commands[1]))
    elif commands[0] == "all":
        for i in range(1, 21):
            S.add(i)
    else:
        S.clear()