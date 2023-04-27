import sys
input=sys.stdin.readline
t=int(input())
m=[25,10,5,1]
for _ in range(t):
    a=int(input())
    res=[]
    for i in m:
        res.append(a//i)
        a%=i
    print(*res)