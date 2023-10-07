import sys
input=sys.stdin.readline
k,n=map(int,input().split())
a=[int(input()) for _ in range(k)]
l,r=1,max(a)
while l<=r:
    mid=(l+r)//2
    line=0
    for i in a:
        line+=i//mid
    if line>=n:
        l=mid+1
    else:
        r=mid-1
print(r)