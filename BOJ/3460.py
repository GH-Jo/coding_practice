T = int(input())
for _ in range(T):
    n = int(input())
    lst = []
    while n > 1:
        n, mod = divmod(n, 2)
        lst.append(mod)
    lst.append(n)

    lst_i = []
    for i, v in enumerate(lst):
        if v == 1:
            lst_i.append(i)
    print(' '.join(map(str, lst_i)))


#---- bin(n) 내장함수를 활용하는 방법
#  n = int(sys.stdin.readline())
#  s = bin(n)[:1:-1]