import sys
input=sys.stdin.readline
n,l=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
start=a[0]
cnt=1
for i in a[1:]:
    if (i+0.5)-(start-0.5)<=l:
        continue
    else:
        start=i
        cnt+=1
print(cnt)