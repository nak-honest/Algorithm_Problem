# 엣지 케이스를 알아내기 어려웠다..
# 두 선이 평행하면서 점 하나를 공통으로 가지고, 한 선이 다른 선을 포함하는 경우를 거르지 못하였다.

# 걸린 시간 : 1시간 40분
# 제출 횟수 : 3번
# 풀이 참조 : x
# 반례 참조 : x

def ccw(a, b, c):
    return a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

def get_cross_point():
    cross_point = [0, 0]
    cross_point[0] = ((a[1] * b[0] - a[0] * b[1]) * (d[0] - c[0]) - (c[1] * d[0] - c[0] * d[1]) * (b[0] - a[0])) \
                     / ((a[1] - b[1]) * (d[0] - c[0]) - (c[1] - d[1]) * (b[0] - a[0]))

    cross_point[1] = ((a[1] * b[0] - a[0] * b[1]) * (c[1] - d[1]) - (c[1] * d[0] - c[0] * d[1]) * (a[1] - b[1])) \
        / ((b[0] - a[0]) * (c[1] - d[1]) - (d[0] - c[0]) * (a[1] - b[1]))

    return cross_point


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a = (x1, y1)
b = (x2, y2)
c = (x3, y3)
d = (x4, y4)

answer = 0
is_more_two_cross_point = False

# x 자 모양으로 교차하는 경우
if ccw(a, b, c) * ccw(a, b, d) < 0 and ccw(c, d, a) * ccw(c, d, b) < 0:
    answer = 1
# L2의 끝점이 L1 위에 있고, L1과 L2가 평행하지 않은 경우
elif ccw(a, b, c) * ccw(a, b, d) == 0 and abs(ccw(a, b, c)) + abs(ccw(a, b, d)) != 0 \
        and ccw(c, d, a) * ccw(c, d, b) < 0:
    answer = 1
# L1의 끝점이 L2 위에 있고, L1과 L2가 평행하지 않은 경우
elif ccw(c, d, a) * ccw(c, d, b) == 0 and abs(ccw(c, d, a)) + abs(ccw(c, d, b)) != 0 \
        and ccw(a, b, c) * ccw(a, b, d) < 0:
    answer = 1
elif ccw(a, b, c) == 0 and ccw(a, b, d) == 0:
    # L1과 L2가 평행하면서 두 선분이 겹치고, L1이 L2보다 왼쪽에 있는 경우.
    if (min(a[0], b[0]) < min(c[0], d[0]) and max(a[0], b[0]) > min(c[0], d[0])) \
            or (min(a[1], b[1]) < min(c[1], d[1]) and max(a[1], b[1]) > min(c[1], d[1])):
        answer = 1
        is_more_two_cross_point = True
    # L1과 L2가 평행하면서 두 선분이 겹치고, L2가 L1보다 왼쪽에 있는 경우.
    elif (min(c[0], d[0]) < min(a[0], b[0]) and max(c[0], d[0]) > min(a[0], b[0])) \
            or (min(c[1], d[1]) < min(a[1], b[1]) and max(c[1], d[1]) > min(a[1], b[1])):
        answer = 1
        is_more_two_cross_point = True

# L1과 L2의 점이 하나라도 겹치는 경우
if len({a, b, c, d}) < 4:
    answer = 1
    # L1과 L2가 같은 점인 경우
    if len({a, b, c, d}) == 2:
        is_more_two_cross_point = True
    # L1과 L2가 평행하고, 한 점이 겹치며, 한 선이 다른 한선을 포함하는 경우
    elif ccw(a, b, c) == 0 and ccw(a, b, d) == 0:
        if min(a[0], b[0]) == min(c[0], d[0]) and min(a[1], b[1]) == min(c[1], d[1]):
            is_more_two_cross_point = True
        elif max(a[0], b[0]) == max(c[0], d[0]) and max(a[1], b[1]) == max(c[1], d[1]):
            is_more_two_cross_point = True

print(answer)
if answer == 1 and not is_more_two_cross_point:
    if len({a, b, c, d}) == 3:
        points = [a, b, c, d]
        for point in {a, b, c, d}:
            points.remove(point)
        print(*points[0])
    else:
        print(*get_cross_point())


'''
r = (p, q) 가 교차점이라고 하자. 일단 x자로 교차하는 경우만 생각하자.
그러면 해당 교차점에 대해서 ccw(a, b, r) == 0 이고 ccw(c, d, r) == 0 인 경우에 점 r이 교차점이 된다.

즉 a[0] * b[1] + b[0] * r[1] + r[0] * a[1] - (a[1] * b[0] + b[1] * r[0] + r[1] * a[0]) = 0
c[0] * d[1] + d[0] * r[1] + r[0] * c[1] - (c[1] * d[0] + d[1] * r[0] + r[1] * c[0]) == 0

(a[1] - b[1]) * r[0] + (b[0] - a[0]) * r[1] = a[1] * b[0] - a[0] * b[1]
(c[1] - d[1]) * r[0] + (d[0] - c[0]) * r[1] = c[1] * d[0] - c[0] * d[1]



(b[0] - a[0]) * (c[1] - d[1]) * r[1] = (a[1] * b[0] - a[0] * b[1]) * (c[1] - d[1])
(d[0] - c[0]) * (a[1] - b[1]) * r[1] = (c[1] * d[0] - c[0] * d[1]) * (a[1] - b[1])

((b[0] - a[0]) * (c[1] - d[1]) - (d[0] - c[0]) * (a[1] - b[1])) * r[1] 
= (a[1] * b[0] - a[0] * b[1]) * (c[1] - d[1]) - (c[1] * d[0] - c[0] * d[1]) * (a[1] - b[1])

r[1] = (a[1] * b[0] - a[0] * b[1]) * (c[1] - d[1]) - (c[1] * d[0] - c[0] * d[1]) * (a[1] - b[1]) / ((b[0] - a[0]) * (c[1] - d[1]) - (d[0] - c[0]) * (a[1] - b[1]))



(a[1] - b[1]) * r[0] + (b[0] - a[0]) * r[1] = a[1] * b[0] - a[0] * b[1]
(c[1] - d[1]) * r[0] + (d[0] - c[0]) * r[1] = c[1] * d[0] - c[0] * d[1]

(a[1] - b[1]) * (d[0] - c[0]) * r[0] = (a[1] * b[0] - a[0] * b[1]) * (d[0] - c[0])
(c[1] - d[1]) * (b[0] - a[0]) * r[0] = (c[1] * d[0] - c[0] * d[1]) * (b[0] - a[0])

((a[1] - b[1]) * (d[0] - c[0]) - (c[1] - d[1]) * (b[0] - a[0])) * r[0] 
= ((a[1] * b[0] - a[0] * b[1]) * (d[0] - c[0]) - (c[1] * d[0] - c[0] * d[1]) * (b[0] - a[0]))

r[0] = ((a[1] * b[0] - a[0] * b[1]) * (d[0] - c[0]) - (c[1] * d[0] - c[0] * d[1]) * (b[0] - a[0])) / ((a[1] - b[1]) * (d[0] - c[0]) - (c[1] - d[1]) * (b[0] - a[0]))

이 연립 방정식의 해가 교차점이 된다.

'''
