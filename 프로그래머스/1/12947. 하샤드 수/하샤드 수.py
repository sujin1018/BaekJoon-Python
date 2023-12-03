def solution(x):
    a=list(str(x))
    res=0
    for i in a:
        res+=int(i)
    if x%res==0:
        answer=True
    else: answer=False
    return answer