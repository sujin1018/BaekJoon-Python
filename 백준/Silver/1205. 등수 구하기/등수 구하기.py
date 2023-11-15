n,t,p=map(int,input().split())
if n==0:
    print(1)
else:
    a=list(map(int,input().split()))
    if n==p and a[-1]>=t:
        print(-1)
    else:
        res=n+1
        for i in range(n):
            if a[i]<=t:
                res=i+1
                break
        print(res)