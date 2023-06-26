s = input()
# ASCII : a = 97, z = 123
print(*[s.find(chr(i)) for i in range(97, 123)])