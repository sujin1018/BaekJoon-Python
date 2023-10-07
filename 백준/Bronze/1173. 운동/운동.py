N,m,M,T,R=map(int,input().split())
x=m
cnt=t=0
if m+T>M:
    print(-1)
else:
    while cnt<N:
        if x+T<=M:
            x+=T
            cnt+=1
        else:
            x=max(x-R,m)
        t+=1
    print(t)