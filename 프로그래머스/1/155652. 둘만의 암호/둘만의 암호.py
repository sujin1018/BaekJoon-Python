def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for sk in skip:
        alpha = alpha.replace(sk, '')
    for i in s: 
        answer += alpha[(alpha.index(i) + index) % len(alpha)]     
    return answer