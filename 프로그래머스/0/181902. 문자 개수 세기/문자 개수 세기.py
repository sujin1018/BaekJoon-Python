def solution(my_string):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    answer = [0] * 52
    for i in my_string:
        answer[alpha.index(i)] += 1
    return answer