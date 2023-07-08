import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    a=[list(map(int,input().split())) for _ in range(n)]
    a.sort()
    res=a[0][1]
    cnt=1
    for i in range(1,n):
        if a[i][1]<res:
            res=a[i][1]
            cnt+=1
    print(cnt)