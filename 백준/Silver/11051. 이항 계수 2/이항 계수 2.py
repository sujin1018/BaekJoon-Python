n,k=map(int,input().split())
def fac(x):
    res=1
    for i in range(1,x+1):
        res*=i
    return res
res=fac(n)//(fac(k)*fac(n-k))
print(res%10007)