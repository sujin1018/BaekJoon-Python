import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
    h,w,n=map(int,input().split())
    f=n%h
    r=n//h+1
    if f==0:
        f=h
        r-=1
    print(f*100+r)