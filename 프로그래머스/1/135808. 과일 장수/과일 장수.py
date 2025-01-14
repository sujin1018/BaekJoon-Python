def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    # 방법 1
    for i in range(len(score)//m):
        answer += score[(i + 1) * m - 1] * m
    # 방법 2    
    # for i in range(0, len(score), m):
    #     if len(score[i : i + m]) == m:
    #         answer += min(score[i : i + m]) * m
    return answer