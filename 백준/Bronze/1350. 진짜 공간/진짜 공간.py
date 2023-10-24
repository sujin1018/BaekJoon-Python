n=int(input())
f=list(map(int,input().split()))
c=int(input())
res=0
for i in f:
    if i!=0 and i<=c:
        res+=1
    elif i==0:
        continue
    else:
        if i%c!=0:
            res+=(i//c)+1
        else:
            res+=(i//c)
print(c*res)