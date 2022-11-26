cnt = 0
for i in range(8):
    if i % 2 == 0:
        init = 0
    else:
        init = 1
    line = list(input())
    for j in range(init, 8, 2):
        cnt += int(line[j] == 'F')
print(cnt)
         