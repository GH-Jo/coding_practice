def solution(s):
    numdic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 
              'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', }
    for i in numdic.keys():
        while i in s:
            idx = s.index(i)
            s = s[:idx] + numdic[i] + s[idx+len(i):]
        
    return int(s)