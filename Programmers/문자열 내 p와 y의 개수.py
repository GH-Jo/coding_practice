def solution(s):
    num_n = sum([1 for c in s.lower() if c == 'p'])
    num_p = sum([1 for c in s.lower() if c == 'y'])
    return num_n == num_p

### 다른 사람의 풀이 ###
"""
def solution(s):
    return s.lower().count('p') == s.lower().count('y')

from collections import Counter
def solution(s):
    c = Counter(s.lower())
    return c['y'] == c['p']
"""
