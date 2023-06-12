import sys
input=sys.stdin.readline
n=int(input())
d={}
for i in range(n):
    s=input().rstrip().split('.')[1]
    if s in d:
        d[s]+=1
    else:
        d[s]=1
res=sorted(d.items())
for k,v in res:
    print(k,v)