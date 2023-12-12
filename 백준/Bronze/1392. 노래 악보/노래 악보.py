import sys
input=sys.stdin.readline
n,q=map(int,input().split())
a=[int(input()) for _ in range(n)]
b=[int(input()) for _ in range(q)]
res=[]
i=1
for x in a:
    for _ in range(x):
        res.append(i)
    i+=1
for i in b:
    print(res[i])