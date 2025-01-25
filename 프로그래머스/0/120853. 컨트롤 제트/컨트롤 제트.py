def solution(s):
    answer = 0
    data = list(s.split())
    for i in range(len(data)):
        if data[i] == 'Z':
            answer -= int(data[i-1])
        else:
            answer += int(data[i])
    return answer