def solution(a, b, c, d):
    d=[a,b,c,d]
    s=list(set(d));
    answer = 0
    if len(s)==1:
        answer=1111*a
    elif len(s)==4:
        answer=min(s)
    elif len(s)==3:
        p=max(d,key=d.count)
        tmp=[i for i in s if i!=p]
        answer=tmp[0]*tmp[1]
    elif len(s)==2:
        if max([d.count(i) for i in s])>2:
            p=max(d,key=d.count)
            q=min(d,key=d.count)
            answer=((10*p)+q)**2
        else:
            answer=(s[0]+s[1])*abs(s[0]-s[1])
    return answer