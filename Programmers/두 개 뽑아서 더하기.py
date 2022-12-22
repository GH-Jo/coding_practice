# https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    idxs = [(i,j) for i in range(len(numbers)) for j in range(len(numbers)) if i!=j]
    answer = set([numbers[i]+numbers[j] for i,j in idxs])
    return sorted(answer)