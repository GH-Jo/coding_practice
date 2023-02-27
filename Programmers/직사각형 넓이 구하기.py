def solution(dots):
    xs = [dots[i][0] for i in range(len(dots))]
    ys = [dots[i][1] for i in range(len(dots))]
    return (max(xs)- min(xs)) * (max(ys)- min(ys))