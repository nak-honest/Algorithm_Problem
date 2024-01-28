# 엣지 케이스 처리가 까다로웠다..

# 걸린 시간 : 40분
# 제출 횟수 : 5번
# 풀이 참조 : x
# 반례 참조 : x

def ccw(a, b, c):
    return a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0])

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a = (x1, y1)
b = (x2, y2)
c = (x3, y3)
d = (x4, y4)

# x 자 모양으로 교차하는 경우
if ccw(a, b, c) * ccw(a, b, d) < 0 and ccw(c, d, a) * ccw(c, d, b) < 0:
    print(1)
# L2의 끝점이 L1 위에 있고, L1과 L2가 평행하지 않은 경우
elif ccw(a, b, c) * ccw(a, b, d) == 0 and abs(ccw(a, b, c)) + abs(ccw(a, b, d)) != 0 \
        and ccw(c, d, a) * ccw(c, d, b) < 0:
    print(1)
# L1의 끝점이 L2 위에 있고, L1과 L2가 평행하지 않은 경우
elif ccw(c, d, a) * ccw(c, d, b) == 0 and abs(ccw(c, d, a)) + abs(ccw(c, d, b)) != 0 \
        and ccw(a, b, c) * ccw(a, b, d) < 0:
    print(1)
# L1과 L2의 점이 하나라도 겹치는 경우
elif len({a, b, c, d}) < 4:
    print(1)
elif ccw(a, b, c) == 0 and ccw(a, b, d) == 0:
    # L1과 L2가 평행하면서 두 선분이 겹치고, L1이 L2보다 왼쪽에 있는 경우.
    if (min(a[0], b[0]) < min(c[0], d[0]) and max(a[0], b[0]) > min(c[0], d[0])) \
            or (min(a[1], b[1]) < min(c[1], d[1]) and max(a[1], b[1]) > min(c[1], d[1])):
        print(1)
    # L1과 L2가 평행하면서 두 선분이 겹치고, L2가 L1보다 왼쪽에 있는 경우.
    elif (min(c[0], d[0]) < min(a[0], b[0]) and max(c[0], d[0]) > min(a[0], b[0])) \
            or (min(c[1], d[1]) < min(a[1], b[1]) and max(c[1], d[1]) > min(a[1], b[1])):
        print(1)
    # L1과 L2가 평행하지만 겹치지 않는 경우
    else:
        print(0)
else:
    print(0)
