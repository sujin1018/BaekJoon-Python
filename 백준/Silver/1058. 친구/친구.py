import sys
input=sys.stdin.readline
n=int(input())
a=[list(input().rstrip()) for _ in range(n)]
s=[[0]*n for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if a[i][j]=='Y' or (a[i][k]=='Y' and a[k][j]=='Y'):
                s[i][j]=1
res=0
for i in s:
    res=max(res,sum(i))
print(res)