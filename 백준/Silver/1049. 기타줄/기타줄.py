import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(m)]
six=sorted(a,key=lambda x:x[0])
one=sorted(a,key=lambda x:x[1])
res=0
if six[0][0] <= one[0][1]*6:
    res=six[0][0] *(n//6) + one[0][1]*(n%6)
    if six[0][0] < one[0][1]*(n%6):
        res=six[0][0]*(n//6+1)
else:
    res=one[0][1]*n
print(res)