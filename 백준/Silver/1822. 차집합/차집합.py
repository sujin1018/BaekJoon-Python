import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
res=sorted(a-b)
if len(res)==0:
    print(0)
else:
    print(len(res))
    print(*res)