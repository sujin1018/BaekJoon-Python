import sys
m,n=map(int,sys.stdin.readline().split())
def prime(x):
    if x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
for i in range(m,n+1):
    if(prime(i)):
        print(i)