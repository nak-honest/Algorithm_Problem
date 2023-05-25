import sys

n = int(input())
records = [sys.stdin.readline().split() for _ in range(n)]
records_dict = {name: commute for name, commute in records}
people_entered = list(filter(lambda k: records_dict[k] == "enter", records_dict.keys()))

print(*sorted(people_entered, reverse=True))