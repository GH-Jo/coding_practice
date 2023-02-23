def solution(keyinput, board):
    pos = [0, 0]
    dic = {'up':[0,1], 'down':[0,-1],
          'left':[-1,0], 'right':[1,0]}
    xlim, ylim = board[0]//2, board[1]//2
    for k in keyinput:
        x, y = pos
        dx, dy = dic[k]
        x = max(-xlim, min(x+dx, xlim))
        y = max(-ylim, min(y+dy, ylim))
        pos = x, y
    return pos
        
    return answer