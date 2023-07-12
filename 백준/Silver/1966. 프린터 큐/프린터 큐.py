import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    idx=list(range(n))
    cnt=0
    while True:
        if a[0]==max(a):
            cnt+=1
            if idx[0]==m:
                print(cnt)
                break
            else:
                a.pop(0)
                idx.pop(0)
        else:
            a.append(a.pop(0))
            idx.append(idx.pop(0))