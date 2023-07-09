# 이 문제는 페르마의 소정리 내용을 보고나서 풀려고해도 잘 풀리지 않았다.
# 페르마의 소정리에서 모듈로 역원에 대한 부분이 잘 이해가 가지 않아서 못 풀었다.

# p가 소수이고 a가 p보다 작은 정수일때 다음을 만족한다.
# a^p mod p == a mod p
# a^(p-1) mod p == 1 mod p == 1
# a^(-1) mod p == a^(p-2) mod p

# b도 p보다 작은 정수일때 다음을 만족한다.
# (a / b) mod p == a * b^(-1) mod p == (a mod p) * (b^(-1) mod p) mod p == (a mod p) * (b^(p-2) mod p) mod p

# 따라서 n과 k가 p보다 작은 정수라면, nCk % p를 다음과 같이 구할수 있다.
# nCk % p == (n! / (k! * (n-k)!)) % p == ((n! % p) * ((k! * (n-k)!) ^ (-1) % p)) % p
# == ((n! % p) * ((k! * (n-k)!) ^ (p-2) % p)) % p 이다.


N, K = map(int, input().split())
P = 1_000_000_007


# n! % p 를 반환한다.
def factorial_modulo(n, p):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % p

    return result


# n^x % p 를 반환한다.
def get_power(n, x, p):
    if x == 1:
        return n % p

    half = get_power(n, x // 2, p)
    if x % 2 == 0:
        return (half * half) % p
    else:
        return (half * half * n) % p


base = (factorial_modulo(K, P) * factorial_modulo(N-K, P)) % P
answer = (factorial_modulo(N, P) * get_power(base, P-2, P)) % P
print(answer)
