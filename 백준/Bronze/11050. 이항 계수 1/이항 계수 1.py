n,k=map(int,input().split())
def fac(x):
    res=1
    for i in range(1,x+1):
        res*=i
    return res
print(int(fac(n)/(fac(k)*fac(n-k))))