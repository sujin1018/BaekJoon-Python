def solution(survey, choices):
    answer = ''
    mbti = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    for i in range(len(choices)):
        if choices[i] > 4:
            mbti[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            mbti[survey[i][0]] += 4 - choices[i]
    k = list(mbti.keys())
    for i in range(0,len(k),2):
        if mbti[k[i]] >= mbti[k[i+1]]:
            answer += k[i]
        else:
            answer += k[i+1]
    return answer