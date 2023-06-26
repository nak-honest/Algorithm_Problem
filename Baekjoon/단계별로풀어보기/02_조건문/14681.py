x, y = map(int, open(0))

quadrant = {(True, True): 1, (False, True): 2, (False, False): 3, (True, False): 4}
print(quadrant[(x > 0, y > 0)])
