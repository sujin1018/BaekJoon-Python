n=int(input())
a=sorted(list(map(int,input().split())))
x=int(input())
res=0
l,r=0,n-1
while l<r:
    k=a[l]+a[r]
    if k==x:
        res+=1
        l+=1
    elif k<x:
        l+=1
    else:
        r-=1
print(res)