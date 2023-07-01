import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    m=int(input())
    a={}
    for _ in range(m):
        x,y=input().split()
        if y in a.keys():
            a[y]+=1
        else:
            a[y]=1
    cnt=1
    for i in a:
        cnt*=(a[i]+1)
    print(cnt-1)