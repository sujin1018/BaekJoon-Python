import sys
input=sys.stdin.readline
u,n=map(int,input().split())
a=[[] for _ in range(10001)]
b=[0 for _ in range(10001)]
m=10001
for _ in range(n):
    s,p=input().split()
    a[int(p)].append(s)
    b[int(p)]+=1
for i in range(10001):
    if b[i]!=0:
        m=min(b[i],m)
for i in range(10001):
    if m==b[i]:
        print(a[i][0],i)
        break