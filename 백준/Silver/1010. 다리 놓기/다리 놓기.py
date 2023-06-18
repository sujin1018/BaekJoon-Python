import sys
input=sys.stdin.readline
t=int(input())
def fac(x):
    res=1
    for i in range(1,x+1):
        res*=i
    return res
for i in range(t):
    n,m=map(int,input().split())
    res=fac(m)//(fac(m-n)*fac(n))
    print(res)