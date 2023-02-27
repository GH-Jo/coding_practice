def check_board(board, i, j):
    n = len(board)
    for x in range(max(i-1, 0), min(i+2, n)):
        for y in range(max(j-1, 0), min(j+2, n)):
            board[x][y] = 1
            
def count_one(board):
    total = 0
    for row in board:
        total += sum(row)
    return total
            
def solution(board):
    shape = len(board), len(board[0])
    board_new = [[0 for i in range(shape[1])] for j in range(shape[0])]
    for i in range(shape[0]):
        for j in range(shape[1]):
            if board[i][j] == 1:
                check_board(board_new, i, j)
    return shape[0]*shape[1] - count_one(board_new)
                
