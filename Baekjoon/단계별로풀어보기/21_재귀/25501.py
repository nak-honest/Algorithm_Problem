def is_palindrome_rec(s, l, r, count):
    count[0] += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    return is_palindrome_rec(s, l+1, r-1, count)


def is_palindrome(s):
    count = [0]
    return [is_palindrome_rec(s, 0, len(s)-1, count), count[0]]


T = int(input())
for _ in range(T):
    print(*is_palindrome(input()))
