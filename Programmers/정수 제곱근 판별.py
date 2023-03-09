def solution(n):
    remainder = n**0.5 % 1
    if remainder == 0:
        return (n**0.5+1)**2
    else:
        return -1

""" 두 번째 풀이
def solution(n):
    i = 1
    while i ** 2 <= n:
        if i ** 2 == n:
            return (i+1) ** 2
        i += 1
    return -1
"""