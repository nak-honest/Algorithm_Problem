grade_dict = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

takes = [list(input().split()) for _ in range(20)]

mul_grade_and_credit = []
course_credits = []

# 등급이 P가 아닌 과목들만 가지고 온다.
for take in filter(lambda t: t[2] != 'P', takes):
    credit = float(take[1])
    grade = grade_dict[take[2]]

    mul_grade_and_credit.append(grade*credit)
    course_credits.append(credit)

print(sum(mul_grade_and_credit)/sum(course_credits))