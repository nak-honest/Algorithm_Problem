T, *case = map(int, open(0).read().split())
answer = [[c//25, c%25//10, c%25%10//5, c%25%10%5] for c in case]

for num in answer:
    print(*num)