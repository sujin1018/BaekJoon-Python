n,m=map(int,input().split())
if n==0:
    print(0)
else:
    a=list(map(int,input().split()))
    res=0
    cnt=1
    for i in a:
        if res+i>m:
            cnt+=1
            res=i
        else:
            res+=i
    print(cnt)