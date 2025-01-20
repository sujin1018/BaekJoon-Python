def solution(X, Y):
    answer = ''
    # 방법 1
    for i in range(9, -1, -1) :
        answer += ( str(i) * min(X.count(str(i)), Y.count(str(i))) )
    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer
    # 방법 2
    # a = sorted(list(set(X) & set(Y)), reverse = True)
    # if len(a) == 0:
    #     return '-1'
    # elif len(a) == a.count('0'):
    #     return '0'
    # for i in a:
    #     answer += i * min(X.count(i), Y.count(i))
    # return answer