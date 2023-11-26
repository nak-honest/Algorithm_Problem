M = 1234567891
r = 31

L = int(input())
seq = [ord(ch) - 96 for ch in ''.join(input())]
power_of_r = [1]

for i in range(1, 50):
    power_of_r.append(power_of_r[-1] * r)
    power_of_r[i] %= M

answer = 0
for i in range(len(seq)):
    answer += seq[i] * power_of_r[i]
    answer %= M

print(answer)