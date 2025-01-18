def solution(s):
    answer = 0
    x,y = 0,0
    for i in s:
        if x == y:
            answer += 1
            first = i
        if i == first:
            x += 1
        else:
            y += 1
    return answer