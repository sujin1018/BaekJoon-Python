import sys
input=sys.stdin.readline
n=int(input())
a=[int(input()) for _ in range(n)]
l=r=1
lm,rm=a[0],a[-1]
for i in range(1,n):
    if a[i]>lm:
        l+=1
        lm=a[i]
for i in range(n-1,-1,-1):
    if a[i]>rm:
        r+=1
        rm=a[i]
print(l)
print(r)