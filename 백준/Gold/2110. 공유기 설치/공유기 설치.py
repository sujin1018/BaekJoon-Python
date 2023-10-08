import sys
input=sys.stdin.readline
n,c=map(int,input().split())
a=[int(input()) for _ in range(n)]
a.sort()
l,r=1,a[-1]-a[0]
res=0
while l<=r:
    mid=(l+r)//2
    cnt=1
    now=a[0]
    for i in range(1,n):
        if a[i]-now>=mid:
            cnt+=1
            now=a[i]
    if cnt>=c:
        l=mid+1
        res=mid
    else:
        r=mid-1
print(res)