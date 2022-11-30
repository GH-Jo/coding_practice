def solution(chicken):
    service = 0
    while chicken >= 10:
        service += 1
        chicken -= 9
    return service


#############################


def solution(chicken):
    service = (chicken-1) // 9
    if service < 0:
        service = 0
    return service


##  다른 사람 풀이 // 재귀함수  ##


def solution(chicken):
    if chicken >= 10:
        return chicken // 10 + solution(chicken//10 + chicken%10)
    else:
        return 0