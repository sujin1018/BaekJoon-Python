n=int(input())
res=0
for i in range(1,n+1):
    a=list(map(int,str(i)))
    res=sum(a)+i
    if res==n:
        print(i)
        break
    if i==n:
        print(0)