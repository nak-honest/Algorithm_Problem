# 피보나치의 성질을 검색해서 도가뉴 항등식을 만족한다는 것을 알게 되었다.
# 혼자서 풀려고 했다면 이 규칙을 찾는데 엄청난 시간을 소모했을것 같다.

# 도가뉴 항등식은 다음과 같다.
# fm+n = fm-1 * fn + fm * fn+1
# 이를 응용하면 다음과 같이 짝수와 홀수에 대한 피보나치 수를 빠르게 구할 수 있다.
# f2n = (fn+1)^2 - (fn-1)^2
# f2n+1 = fn^2 + (fn+1)^2

# 이외에 행렬의 거듭제곱을 이용한 풀이도 존재한다.


p = 1_000_000_007

f = dict()
f[0] = 0
f[1] = 1
f[2] = 1
f[3] = 2

def get_fibonacci(n):
    if n in f:
        return f[n]
    half = n // 2

    if n % 2 == 0:
        f[n] = (get_fibonacci(half+1) ** 2 - get_fibonacci(half-1) ** 2) % p
    else:
        f[n] = (get_fibonacci(half) ** 2 + get_fibonacci(half+1) ** 2) % p

    return f[n]


print(get_fibonacci(int(input())))
