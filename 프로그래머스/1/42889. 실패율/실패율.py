def solution(N, stages):
    answer = []
    fail = {} # 실패율
    players = len(stages) # 전체 플레이어 수
    for i in range(1, N+1):
        if players == 0:
            fail[i] = 0
        else:
            fail[i] = stages.count(i)/players
            players -= stages.count(i)
    answer = sorted(fail, key = lambda x: fail[x], reverse = True)
    return answer