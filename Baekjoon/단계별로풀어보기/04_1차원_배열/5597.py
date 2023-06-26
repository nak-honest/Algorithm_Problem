submit = {int(input()) for _ in range(28)}
attend = {i for i in range(1, 31)}

print(*sorted(attend - submit), sep='\n')