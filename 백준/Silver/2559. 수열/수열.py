import sys
input=sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))
s=sum(a[:k])
res=[s]
for i in range(n-k):
    s=s-a[i]+a[i+k]
    res.append(s)
print(max(res))