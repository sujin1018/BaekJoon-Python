import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[0]*n
for _ in range(m):
    i,j,k=map(int,input().split())
    for y in range(i-1,j):
        a[y]=k
for i in a:
    print(i,end=' ')