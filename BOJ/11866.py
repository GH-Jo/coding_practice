N, K = map(int, input().split())
arr1 = [*range(1, N+1)]
arr2 = []
K2 = 0 
while arr1 != []:
    K2 += K-1
    while K2 >= len(arr1):
        K2 -= len(arr1)
    arr2.append(arr1.pop(K2))

print(f'<{", ".join(map(str, arr2))}>')