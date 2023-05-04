X, N, *receipt = map(int, open(0).read().split())

# 영수증의 물건 가격(짝수 index)와 개수(홀수 index)를 곱해서 더한다
total = sum([receipt[2*i] * receipt[2*i+1] for i in range(N)])
# total = sum(map(lambda a, b: a * b, receipt[0::2], receipt[1::2]))

print(["No", "Yes"][int(X == total)])