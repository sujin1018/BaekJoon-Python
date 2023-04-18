import sys
input=sys.stdin.readline
n,m=map(int,input().split())
d=dict()
for i in range(1,n+1):
    s=input().rstrip()
    d[i]=s
    d[s]=i
for i in range(m):
    a=input().rstrip()
    if a.isdigit():
        print(d[int(a)])
    else:
        print(d[a])