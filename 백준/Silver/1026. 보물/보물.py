import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=0
a.sort()
for i in range(n):
    res+= (a[i] *max(b))
    b.pop(b.index(max(b)))
print(res)

