# solution 1
def solution(n):
    # brute force
    i = 1
    while i < n:
        if n % i == 1:
            return i
        else:
            i += 1
    return -1


# solution 2
def solution(n):    
    # n-1의 약수
    for i in range(2, n):
        if (n-1) % i == 0:
            return i