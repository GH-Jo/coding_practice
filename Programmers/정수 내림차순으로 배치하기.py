# solution 1
def solution(n):
    arr = str(n)
    arr = sorted(arr, reverse=True)
    arr = map(str, arr)
    str1 = ''
    for i in arr:
        str1 += i    
    return int(str1)

# solution 2
def solution(n):
    arr = str(n)
    arr = sorted(arr, reverse=True)
    arr = list(map(int, arr))
    num = 0
    for i in arr:
        num *= 10
        num += i
    return num

# solution 3
from functools import reduce
def solution(n):
    arr = []
    while n > 0:
        arr.append(str(n%10))
        n //= 10
    arr.sort(reverse=True)
    return int(reduce(lambda x, y: x+y, arr, ''))