# 약 한시간 넘게 고민해서 방법이 떠올랐다.
# 분할과 정복 문제라는 것을 알았기 때문에 풀 수 있었지, 그것이 아니라면 못풀었을 것 같다.
# 다른 사람들의 풀이와 큰 틀에서는 동일하지만, 나의 코드가 조금 더 복잡한것 같다.

# 그리고 다음과 같이 한줄로도 풀린다고 한다..
# print(pow(*map(int, input().split())))


A, B, C = map(int, input().split())

# 먼저 exponent = 2**n + r 꼴로 만든다. (여기서 2**n == 2^n)
# 그러면 base ** exponent는 (base ** (2**n)) 와 (base ** r) 의 곱이므로 각각을 구해서 곱해주면 된다.
# 먼저 base ** (2**n) 은 n번의 계산으로 구할수 있다. base를 제곱한 값을 제곱하고, 그 값을 또 제곱하고, ... 이를 n번 하면 된다.
# 즉 base ** (2**n) 은 base를 n번 제곱한 값이라는 것이다.

# base ** r은 또다시 r을 2**n' + r' 꼴로 만들어서 위처럼 구하면 된다. -> 재귀적으로 접근한다.
# 그리고 이렇게 구한 값을 곱하면 된다.

# 마지막으로 (a * b * c) % N == ((a % N) * (b % N) * (c % N)) % N 이므로 위에서 base를 제곱할때마다 dividend로 나눈 나머지를 구한다.
# base ** exponent가 너무 큰 값이기 때문에 미리미리 dividend로 나눈 나머지를 저장시킨다는 것이다.
# 처음에는 dividend를 생각하지 않고 거듭제곱을 빠르게 구하는 방법을 먼저 이해한 뒤 dividend를 살펴보는게 더 잘 이해가 갈것이다.
def get_power(base, exponent, dividend):
    if exponent == 0:
        return 1

    # exponent = 2^n + r 꼴로 나타내기 위해 n과 r을 구한다.
    n = 0
    power_of_two = 1

    while True:
        if power_of_two * 2 < exponent:
            power_of_two *= 2
            n += 1
        else:
            break

    r = exponent - power_of_two

    # square_n_time == (base ** (2**n)) % dividend
    square_n_time = base

    for _ in range(n):
        square_n_time = square_n_time * square_n_time
        # 미리미리 dividend로 나눈 나머지를 저장시킨다.
        square_n_time = square_n_time % dividend

    # return (((base ** (2**n)) % dividend) * ((base ** r) % dividend)) % dividend
    return (square_n_time * get_power(base, r, dividend)) % dividend


print(get_power(A, B, C))
