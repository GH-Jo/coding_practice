def check(n):
    if '3' in str(n):
        return False
    if n % 3 == 0:
        return False
    return True

def solution(n):
    numlist = list(range(1, n+1))
    i = 0
    while i < n:
        if check(numlist[i]):
            i += 1
        else:
            numlist.append(numlist[-1]+1)
            numlist.pop(i)
    return numlist[-1]