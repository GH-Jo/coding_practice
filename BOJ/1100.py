status = []
cnt = 0
for _ in range(8):
    status.append(list(input()))

for i in range(8):
    for j in range(8):
        if (i%2 == 0) and (j%2 == 0):
            cnt += int(status[i][j] == 'F')
        elif (i%2 == 1) and (j%2 == 1):
            cnt += int(status[i][j] == 'F')
print(cnt)
