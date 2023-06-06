import sys
input=sys.stdin.readline
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
a.sort(reverse=True)
res=[]
for i in range(n):
    res.append(a[i]*(i+1))
print(max(res))