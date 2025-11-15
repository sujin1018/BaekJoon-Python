def solution(board, moves):
    lanes=[[] for _ in range(len(board[0]))]
    stack=[]
    answer=0
    for i in range(len(board)-1,-1,-1):
        for j in range(len(board[0])):
            if board[i][j]:
                lanes[j].append(board[i][j])
    for i in moves:
        if lanes[i-1]:
            doll=lanes[i-1].pop()
            if stack and stack[-1]==doll:
                stack.pop()
                answer+=2
            else:
                stack.append(doll)
    return answer