A, B = sorted(map(int, input().split()))
if B-A <= 1:
    print(0)
else:
    print(B-A-1)
    for num in range(A+1, B-1):
        print(num, end=' ')
    print(B-1, end='')
    # 시간 줄이기 #
    # print(" ".join(map(str, interval)))