N, *words = open(0).read().split()

words = set(words)
print(*sorted(words, key=lambda x: (len(x), x)), sep='\n')
