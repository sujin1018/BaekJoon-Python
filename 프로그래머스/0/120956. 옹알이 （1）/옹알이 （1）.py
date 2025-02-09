def solution(babbling):
    word = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling:
        for j in word:
            if j*2 not in i:
                i = i.replace(j, '0')
        if len(i) == i.count('0'):
            answer += 1
    return answer