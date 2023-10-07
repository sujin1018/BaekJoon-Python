import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=list(map(int,input().split()))
l,r=1,max(a)
while l<=r:
    mid=(l+r)//2
    t=0
    for i in a:
        if i>mid:
            t+=i-mid
    if t>=m:
        l=mid+1
    else:
        r=mid-1
print(r)