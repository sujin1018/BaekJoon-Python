import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())
def power(a,b):
    if b==1:
        return a%c
    else:
        res=power(a,b//2)
        if b%2==0:
            return (res*res)%c
        else:
            return (res*res*a)%c
print(power(a,b))