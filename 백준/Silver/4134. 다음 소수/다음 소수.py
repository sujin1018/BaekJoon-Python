import sys
input=sys.stdin.readline
n=int(input())
def prime(x):
    if x==0 or x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
for i in range(n):
    a=int(input())
    while True:
        if prime(a):
            print(a)
            break
        else:
            a+=1