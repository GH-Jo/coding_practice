def solution(absolutes, signs):
    answer = 0
    sign_dic = {True: 1, False: -1}
    signs = [sign_dic[i] for i in signs]
    for i,v in enumerate(signs):
         answer += v * absolutes[i]
    return answer


## 다른 사람 풀이
def solution(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign: 
            answer += absolute
        else: 
            answer -= absolute
    return answer