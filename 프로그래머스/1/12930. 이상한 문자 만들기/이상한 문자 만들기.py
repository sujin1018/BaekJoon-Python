def solution(s):
    answer = []
    s = s.split(' ')
    for word in s:
        res=''
        for i in range(len(word)):
            if i%2==0:
                res += word[i].upper()
            else:
                res += word[i].lower()
        answer.append(res)
    return ' '.join(answer)