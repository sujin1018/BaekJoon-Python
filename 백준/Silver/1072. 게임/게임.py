import sys
input=sys.stdin.readline
x,y=map(int,input().split())
z=(y*100)//x
if z>=99:
    print(-1)
else:
    res=0
    l=0
    r=x
    while l<=r:
        mid=(l+r)//2
        if (y+mid)*100//(x+mid)<=z:
            l=mid+1
        else:
            res=mid
            r=mid-1
    print(res)