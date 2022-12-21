def solution(num, total):
    base = total // num
    answer = list(range(base, base+num ))
    while sum(answer) != total:
        print(answer)
        if sum(answer) > total:
            answer = [i-1 for i in answer]
        elif sum(answer) < total:
            answer = [i+1 for i in answer]
    return answer

num, total = map(int, input().split())
answer = solution(num, total)
print(answer)