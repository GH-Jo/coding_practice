def solution(score):
    avg_lst = [(i+j)/2 for i, j in score]
    rank_lst = []
    for v in avg_lst:
        # v보다 큰 수의 개수를 세서 등수로 적어준다.
        greater = 1
        for v2 in avg_lst:
            if v2 > v:
                greater += 1
        rank_lst.append(greater)
    return rank_lst