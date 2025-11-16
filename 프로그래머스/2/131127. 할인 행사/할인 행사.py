def solution(want, number, discount):
    dict={}
    answer = 0
    for i in range(len(want)):
        dict[want[i]]=number[i]
        
    for i in range(len(discount)-9):
        dict_10={}
        for j in range(i,i+10):
            if discount[j] in dict:
                dict_10[discount[j]]=dict_10.get(discount[j],0)+1
        if dict_10 == dict:
            answer+=1
    return answer