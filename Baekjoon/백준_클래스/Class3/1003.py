'''
fibonacci[0] = [1, 0]
fibonacci[1] = [0, 1]
fibonacci[2] = [1, 1]
fibonacci[3] = [1, 2]
'''

fibonacci = [[1, 0], [0, 1], [1, 1], [1, 2]]

for _ in range(40):
    fibonacci.append([fibonacci[-1][0] + fibonacci[-2][0], fibonacci[-1][1] + fibonacci[-2][1]])

for _ in range(int(input())):
    N = int(input())
    print(*fibonacci[N])
