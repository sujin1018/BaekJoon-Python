def solution(lottos, win_nums):
    win = 0
    rank = [6,6,5,4,3,2,1]
    for i in lottos:
        if i in win_nums:
            win += 1
    return [rank[win + lottos.count(0)], rank[win]]