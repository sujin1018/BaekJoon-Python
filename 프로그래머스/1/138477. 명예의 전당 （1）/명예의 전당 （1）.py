def solution(k, score):
    hall=[]
    answer = []
    for i in score:
        if len(hall) < k:
            hall.append(i)
        else:
            if i > min(hall):
                hall.remove(min(hall))
                hall.append(i)
        answer.append(min(hall))
    return answer