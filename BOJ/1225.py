A, B = input().split()
Alist = list(map(int, list(A)))
Blist = list(map(int, list(B)))

output = 0
for i in Alist:
    result = [i*j for j in Blist]
    output += sum(result) 
print(output)


# 처음에는 list(str) 메서드를 안쓰고 divmod를 활용해서 풀려고 했다.
# 그런데 시간 초과가 떠서 빠른 list(str)으로 돌아갔다.
# 그래도 시간초과가 떴다.
# 시간을 아껴주는 list comprehension을 썼다.
# 그러자 메모리 초과가 났다.
# 그래서 list comprehension을 작은 단위(for문 하나)로 수행하고 
# 결과 합을 중간중간 업데이트해주는 방식으로 해서 통과가 떴다.