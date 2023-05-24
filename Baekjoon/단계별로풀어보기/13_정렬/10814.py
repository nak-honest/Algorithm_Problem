N = int(input())
people = [input().split() for _ in range(N)]

for person in sorted(people, key=lambda x: int(x[0])):
    print(*person)