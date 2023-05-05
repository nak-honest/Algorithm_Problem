N, *scores = map(int, open(0).read().split())

max_score = max(scores)
answer = [score/max_score*100 for score in scores]

print(sum(answer)/len(answer))