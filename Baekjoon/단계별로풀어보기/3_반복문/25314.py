repeat = int(input()) // 4
# print(*["long" for _ in range(repeat)] + ["int"], sep=' ')
print(*(["long"])*repeat, "int", sep=' ')