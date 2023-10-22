import sys
input=sys.stdin.readline
N,L,W,H=map(int,input().split())
l,r=0,max(L,W,H)
for _ in range(100):
    m=(l+r)/2
    if (L//m)*(W//m)*(H//m)>=N:
        l=m
    else:
        r=m
print(l)