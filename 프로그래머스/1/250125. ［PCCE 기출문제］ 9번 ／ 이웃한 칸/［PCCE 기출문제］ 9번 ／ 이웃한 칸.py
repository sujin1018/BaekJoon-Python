def solution(board, h, w):
    answer = 0
    x = [0, 1, -1, 0]
    y = [1, 0, 0, -1]
    
    for i in range(4):
        nx = h + y[i]
        ny = w + x[i]
        if 0 <= nx < len(board) and 0 <= ny < len(board):
            if board[nx][ny] == board[h][w]:
                answer += 1
    return answer