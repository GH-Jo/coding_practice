def solution(arr):
    minval, minidx = arr[0], 0
    for i,v in enumerate(arr):
        if minval > v:
            minidx = i
            minval = v
    arr.pop(minidx)
    if arr == []:
        arr = [-1]
    return arr