import sys
input=sys.stdin.readline
n,k=map(int,input().split())
a=[int(input()) for _ in range(n)]
l,r=1,max(a)
while l<=r:
    mid=(l+r)//2
    res=0
    for i in a:
        res+=i//mid
    if res>=k:
        l=mid+1
    else:
        r=mid-1
print(r)