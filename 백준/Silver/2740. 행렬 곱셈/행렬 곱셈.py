import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
m,k=map(int,input().split())
b=[list(map(int,input().split())) for _ in range(m)]

s=[[0]*k for _ in range(n)]
for r in range(n):
    for c in range(k):
        res=0
        for i in range(m):
            res+=a[r][i]*b[i][c]
        s[r][c]=res
for i in s:
    print(*i)