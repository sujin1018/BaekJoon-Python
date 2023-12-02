import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[list(input()) for _ in range(n)]
s=min(n,m)
res=0
for i in range(n):
    for j in range(m):
        for k in range(s):
            if (i+k)<n and (j+k)<m and (a[i][j]==a[i][j+k]==a[i+k][j]==a[i+k][j+k]):
                res=max(res,(k+1)**2)
print(res)  