import sys, math
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if r1+r2>d and abs(r1-r2)<d: 
        print(2)
    elif r1+r2==d or abs(r1-r2)==d and d!=0: 
        print(1)
    elif d>r1+r2 or d<abs(r1-r2):
        print(0)
    elif d==0 and r1==r2: 
        print(-1)