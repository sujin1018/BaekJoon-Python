import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[i for i in range(1,n+1)]
for i in range(m):
    i,j,k=map(int,input().split())
    a = a[:i-1]+a[k-1:j]+a[i-1:k-1]+a[j:]
for i in a:
    print(i, end=' ')