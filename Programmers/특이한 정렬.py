def solution(numlist, n):
    numlist = sorted(numlist, reverse=True)
    distlist = [abs(i-n) for i in numlist]
    sortedlist = sorted(zip(numlist, distlist), key=lambda x:x[1])
    sortedlist = [i for i, _ in sortedlist]
    return sortedlist