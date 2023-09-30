import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
s=[]
res=[-1]*n
for i in range(n):
    while s and a[s[-1]]<a[i]:
        res[s.pop()]=a[i]
    s.append(i)
print(*res)