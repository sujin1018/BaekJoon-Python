n=int(input())
a=sorted(list(map(int,input().split())))
l,r=0,n-1
ans=abs(a[l]+a[r])
res=[a[l],a[r]]
while l<r:
    i=a[l]
    j=a[r]
    total=i+j
    if abs(total)<ans:
        ans=abs(total)
        res=[i,j]
        if ans==0:
            break
    if total<0:
        l+=1
    else:
        r-=1
print(res[0],res[1])