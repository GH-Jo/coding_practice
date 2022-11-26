N = int(input())
F = int(input())

for i in range(100):
    M = (N // 100) * 100 + i
    if M % F == 0:
        break
print(f"{i:02}")