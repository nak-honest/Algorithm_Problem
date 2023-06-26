a, b = input().split()

a_r = ''.join(reversed(a))
b_r = ''.join(reversed(b))

print(max(int(a_r), int(b_r)))