import sys

N = int(input())
dancing = {'ChongChong': 0}

for _ in range(N):
    A, B = sys.stdin.readline().split()

    if A in dancing or B in dancing:
        dancing[A] = 0
        dancing[B] = 0

print(len(dancing))