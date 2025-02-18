def solution(array):
    mode = 0
    answer = [0] * (max(array) + 1)
    for i in array:
        answer[i] += 1
    for i in answer:
        if i == max(answer):
            mode += 1
    if mode > 1:
        return -1
    return answer.index(max(answer))