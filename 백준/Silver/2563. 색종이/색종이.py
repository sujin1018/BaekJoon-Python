import sys
input=sys.stdin.readline
a=[[0]*101 for _ in range(101)]
res=0
n=int(input())
for _ in range(n):
    r,c=map(int,input().split())
    for i in range(r,r+10):
        for j in range(c,c+10):
            a[i][j]=1
for i in a:
    res+=i.count(1)
print(res)