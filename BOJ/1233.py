from collections import Counter
s1, s2, s3 = map(int, input().split())
lst = []
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            lst.append(i+j+k)

cnt_dict = {}
for n in lst:
    if not cnt_dict.get(n):
        cnt_dict[n]=1
    else:
        cnt_dict[n]+=1

max_v = -1
for k, v in sorted(cnt_dict.items()):
    if v > max_v:
        max_v = v
        max_k = k
print(max_k)