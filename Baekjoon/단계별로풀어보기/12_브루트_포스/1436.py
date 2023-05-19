# 단순히 666 부터 숫자를 1씩 증가시키면서 찾아도 되긴 함.
# 하지만 666이 없는 수까지 모든 수를 다 찾아야 하므로 밑의 코드가 약 10배 이상 효율적임.

N = int(input())
devil_num = '666'
left_digits = '0'  # 666 앞에 붙일 숫자로 1씩 증가한다.
num = ''           # 최종적인 정답이 저장된다.
count = 0

while count < N:
    # left_digits의 마지막 비트가 6이 아니라면 left_digits를 바로 1 증가시켜도 된다.
    if left_digits[-1] != '6':
        count += 1
        num = left_digits + devil_num
        left_digits = str(int(left_digits) + 1)

    # 만약 left_digits의 마지막 비트가 6이라면, left_digits를 바로 1만큼 증가시키면 안된다.
    # 예를들어 '166' + '666' 다음에 바로 '167' + '666'이 되면 안 된다는 것이다.
    # '1' + '666' + '00', '1' + '666' + '01', ... 이러한 숫자들이 더 작기 때문이다.
    else:
        # left_digits의 연속된 뒷자리의 6을 제거한다.
        # 위의 예에서 temp_left_digits = '1'이 된다.
        temp_left_digits = left_digits.rstrip('6')
        # 6이 얼만큼 연속 되었는지를 저장한다.
        sequence_num = len(left_digits) - len(temp_left_digits)

        # 연속된 6이 제거된만큼 right_digits를 0부터 1씩 증가 시킨다.
        # 위의 예에서 right_digits를 00, 01, 02, ..., 99 이렇게 1씩 증가 시킨다.
        for right_digits in range(10 ** sequence_num, 2 * 10 ** sequence_num):
            count += 1
            num = temp_left_digits + devil_num + str(right_digits)[1:]
            if count == N:
                break

        # right_digits가 존재하는 모든 수를 확인했으면, 다시 left_digits를 1 증가시킨다.
        left_digits = str(int(left_digits) + 1)

print(num.lstrip('0'))