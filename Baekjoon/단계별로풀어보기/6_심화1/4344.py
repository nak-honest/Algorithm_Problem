for _ in range(int(input())):
    N, *scores = map(int, input().split())
    avg = sum(scores)/N

    above = list(filter(lambda score: score > avg, scores))
    ratio = len(above)/N * 100

    print('%.3f' % ratio + '%')