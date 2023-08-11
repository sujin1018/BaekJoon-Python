import sys
input=sys.stdin.readline
n=int(input())
r=list(map(int,input().split()))
c=list(map(int,input().split()))
res=r[0]*c[0]
m=c[0]
for i in range(1,n-1):
    if c[i]<m:
        m=c[i]
    res+=m*r[i]
print(res)