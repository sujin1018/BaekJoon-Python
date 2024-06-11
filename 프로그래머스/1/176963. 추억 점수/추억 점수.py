def solution(name, yearning, photo):
    answer = []
    for i in photo:
        cnt = 0
        for j in i:
            if j in name:
                cnt += yearning[name.index(j)]
        answer.append(cnt)
    return answer