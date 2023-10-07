import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
m=int(input())
l,r=0,max(a)
while l<=r:
    mid=(l+r)//2
    res=0
    for i in a:
        if i>mid:
            res+=mid
        else:
            res+=i
    if res<=m:
        l=mid+1
    else:
        r=mid-1
print(r)