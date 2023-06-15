N = int(input())
seq = list(map(int, input().split()))
operations = dict()
for op, num in zip(['+', '-', '*', '//'], input().split()):
    operations[op] = int(num)

min_num = 1000000000
max_num = -1000000000
current_op = [''] * (N-1)


def get_minmax(i):
    if promising(i):
        if i == N - 2:
            global min_num, max_num
            result = seq[0]

            for i in range(N-1):
                if current_op[i] == '+':
                    result += seq[i + 1]
                elif current_op[i] == '-':
                    result -= seq[i + 1]
                elif current_op[i] == '*':
                    result *= seq[i + 1]
                elif current_op[i] == '//' and result >= 0:
                    result = result // seq[i + 1]
                elif current_op[i] == '//' and result < 0:
                    result = -(-result // seq[i + 1])

            min_num = min(min_num, result)
            max_num = max(max_num, result)
        else:
            for op in ['+', '-', '*', '//']:
                current_op[i+1] = op
                get_minmax(i+1)


def promising(i):
    for op in ['+', '-', '*', '//']:
        if current_op[:i+1].count(op) > operations[op]:
            return False
    return True


get_minmax(-1)

print(max_num, min_num, sep='\n')