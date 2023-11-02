import sys
input=sys.stdin.readline
n=int(input())
d=int(input())
cnt=0
a=[int(input()) for _ in range(n-1)]
a.sort(reverse=True)
if n<=1:
    print(0)
else:
    while a[0]>=d:
        d+=1
        a[0]-=1
        cnt+=1
        a.sort(reverse=True)
    print(cnt)