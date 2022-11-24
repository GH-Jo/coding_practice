t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    list1 = [(a**i)%10 for i in range(1, 5)]
    list2 = [10]+list(range(1, 10))
    print(list2[list1[(b-1) % 4]])