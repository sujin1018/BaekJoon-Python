import sys
input=sys.stdin.readline
b,c,d=map(int,input().split())
bb=list(map(int,input().split()))
cc=list(map(int,input().split()))
dd=list(map(int,input().split()))
bb.sort(reverse=True)
cc.sort(reverse=True)
dd.sort(reverse=True)
res=0
min_v=min(b,c,d)
for i in range(min_v):
    res+=(bb[i]+cc[i]+dd[i])*0.9
res+=sum(bb[min_v::])
res+=sum(cc[min_v::])
res+=sum(dd[min_v::])
print(sum(bb)+sum(cc)+sum(dd))
print(int(res))