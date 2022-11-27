N = int(input())
players = {}
for _ in range(N):
    lastname = input()[0]
    if lastname in players:
        players[lastname] += 1
    else:
        players[lastname] = 1

str1 = ''
for k, v in players.items():
    if v >= 5:
        str1 += k

if len(str1) == 0:
    print('PREDAJA')
else:
    print(''.join(sorted(str1))) 