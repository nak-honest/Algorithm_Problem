a, b = input().split()
print(*filter(lambda x: eval(a + x + b), ['>', '<', '==']))