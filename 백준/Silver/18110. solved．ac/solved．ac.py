import sys
input=sys.stdin.readline
def round2(x):
    return int(x)+1 if x-int(x)>=0.5 else int(x)
n=int(input())
if n==0:
    print(0)
else:
    a=[int(input()) for _ in range(n)]
    a.sort()
    ex=round2(n*0.15)
    res=a[ex:n-ex]
    print(round2(sum(res)/len(res)))