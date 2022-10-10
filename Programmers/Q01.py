def solution(s, n):
    lower = ','.join('abcdefghijklmnopqrstuvwxyz').split(',')
    upper = ','.join('ABCDEFGHIJKLMNOPQRSTUVWXYZ').split(',')
    s = ','.join(s).split(',')

    for i in range(len(s)):
        if s[i] in lower:
            if lower.index(s[i]) + n <= 25:
                s[i] = lower[lower.index(s[i]) + n]
            else:
                s[i] = lower[lower.index(s[i]) + n - 26]
        elif s[i] in upper:
            if upper.index(s[i]) + n <= 25:
                s[i] = upper[upper.index(s[i]) + n]
            else:
                s[i] = upper[upper.index(s[i]) + n - 26]
        else:
            continue
    return ''.join(s)


def solution2(s, n):
    lower = ','.join('abcdefghijklmnopqrstuvwxyz').split(',')
    upper = ','.join('ABCDEFGHIJKLMNOPQRSTUVWXYZ').split(',')
    s = ','.join(s).split(',')

    for i in range(len(s)):
        if s[i] in lower:
            s[i] = lower[(lower.index(s[i]) + n) % 26]
        elif s[i] in upper:
            s[i] = upper[(upper.index(s[i]) + n) % 26]
        else:
            continue
    return ''.join(s)

def solution3(s,n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A')+n)%26+ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return "".join(s)

x1 = "AB"
x2 = "z"
x3 = "aBz"

print(solution3(x3, 4))
