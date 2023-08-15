m=int(input())
n=int(input())
res=0
min=n*n
for i in range(1,n):
    if m<=i*i and i*i<=n:
        res+=i*i
        if (i*i<=min):
            min=i*i
if res==0:
    print(-1)
else:
    print(res)
    print(min)