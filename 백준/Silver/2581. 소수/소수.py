import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
res,mp=0,0
def prime(x):
    if x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
for i in range(n,m+1):
    if(prime(i)):
        if(res==0):
            mp=i
        res+=i
if(res==0 and mp==0):
    print(-1)
else:
    print(res,mp,sep='\n')