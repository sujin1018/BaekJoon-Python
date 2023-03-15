n=int(input())
a=list(map(int,input().split()))
b=list()
def prime(x):
    if x==1:
        return False
    for i in range(2,x):
        if(x%i==0):
            return False
    return True
for i in a:
    b.append(prime(i))
print(b.count(True))