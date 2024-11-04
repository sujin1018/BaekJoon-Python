def solution(arr):
    result=[]
    ptrn=[[1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]]
    score=[0]*3
    for i, ans in enumerate(arr):
        for j, pt in enumerate(ptrn):
            if ans==pt[i%len(pt)]:
                score[j]+=1
    max_score=max(score)
    for i,sc in enumerate(score):
        if sc==max_score:
            result.append(i+1)
    return result
