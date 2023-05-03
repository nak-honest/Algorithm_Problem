dice = list(map(int, input().split()))

triple = lambda d: 10000+d.pop()*1000
double = lambda d: 1000+(sum(d)-sum(set(d)))*100
single = lambda d: max(d)*100

lambda_list = [0, triple, double, single]
answer_lambda = lambda_list[len(set(dice))]

print(answer_lambda(dice))