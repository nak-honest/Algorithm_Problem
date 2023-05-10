s = input()

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for c in cro:
    s = s.replace(c, 'a')

print(len(s))