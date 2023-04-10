import sys
input=sys.stdin.readline
n,m=map(int,input().split())
s=[i+1 for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    s[a-1],s[b-1]=s[b-1],s[a-1]
for i in s:
    print(i, end=' ')