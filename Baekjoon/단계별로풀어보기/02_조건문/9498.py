my_score = int(input())
scores = [90, 80, 70, 60, 0]
credit = {90: 'A', 80: 'B', 70: 'C', 60: 'D', 0: 'F'}

score = list(filter(lambda x: my_score >= x, scores))[0]
print(credit[score])
