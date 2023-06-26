input_list = [input() for _ in range(int(input()))]
answer = [sum(map(int, s.split())) for s in input_list]

print(*answer, sep='\n')