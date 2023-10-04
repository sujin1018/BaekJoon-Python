import sys
input=sys.stdin.readline
l=int(input())
s=sorted(list(map(int,input().split())))
n=int(input())
if n in s:
    print(0)
else:
    a,b=0,0
    for i in s:
        if i<n:
            a=i
        elif i>n:
            b=i
            break
    print((n-a)*(b-n)-1)