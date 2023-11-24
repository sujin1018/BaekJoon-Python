import sys
input=sys.stdin.readline
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][j]==1 or (a[i][k]==1 and a[k][j]==1):
                a[i][j]=1
for i in a:
    print(*i)