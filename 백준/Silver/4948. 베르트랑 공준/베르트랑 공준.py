import sys
def prime(x):
    if x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
a=[]
for i in range(2,2*123457):
    if prime(i):
        a.append(i)
while True:
    cnt=0
    n=int(input())
    if n==0:
        break
    for i in a:
        if i>n and i<=2*n:
            cnt+=1
    print(cnt)