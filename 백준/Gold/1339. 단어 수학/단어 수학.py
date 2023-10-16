import sys
input=sys.stdin.readline
n=int(input())
s=[input().rstrip() for _ in range(n)]
a={}
for i in s:
    square_root=len(i)-1
    for j in i:
        if j in a:
            a[j]+=10**square_root
        else:
            a[j]=10**square_root
        square_root-=1
a=sorted(a.values(),reverse=True)
res,m=0,9
for val in a:
    res+=val*m
    m-=1
print(res)