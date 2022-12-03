N, K = map(int, input().split())
cnt = 0
i = 1
while i <= N:
    if N % i == 0:
        cnt += 1
        if cnt == K:
            print(i)
            break
    i += 1
if cnt < K:
    print(0)



# --- if문 줄이기 위해 모든 약수를 구함


N, K = map(int, input().split())
li = []
i = 1
while i <= N:
    if N % i == 0:
       li.append(i)
    i += 1
print(li[K-1] if len(li)>=K else 0) 
