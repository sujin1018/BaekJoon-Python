import sys
input=sys.stdin.readline
n,m=map(int,input().split())
d={}
for i in range(n):
    s=input().rstrip()
    if len(s)>=m:
        if s in d:
            d[s]+=1
        else:
            d[s]=1            
res=sorted(d.items(), key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in res:
    print(i[0])