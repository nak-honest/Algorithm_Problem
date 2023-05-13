from math import ceil

# 길이가 1씩 증가할때마다 방의 개수 = [1, 6*1, 6*2, 6*3, ...]
# 길이 k의 방의 총 합 = 1 + 6*(1 + 2 + 3 + ... + k) = 6 * k*(k+1)/2 + 1
# N번 방의 길이 k는 6 * k*(k+1)/2 + 1 >= N을 만족하는 가장 작은 정수이다.
# k*(k+1) >= (N-1)/3
# k^2 + k + 1/4 >= (N-1)/3 + 1/4
# (k + 1/2)^2 >= (N-1)/3 + 1/4
# k + 1/2 >= root((N-1)/3 + 1/4)
# k >= root((N-1)/3 + 1/4) - 1/2 를 만족하는 가장 작은 정수 k는
# k = ceil(root((N-1)/3 + 1/4) - 1/2)
# 정답은 1을 포함해서 몇개의 방을 지나가는가를 말하기 때문에 k+1이 정답이다.
print(ceil(((int(input())-1)/3+1/4)**(1/2)-0.5)+1)

