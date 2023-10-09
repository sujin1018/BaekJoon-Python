n=int(input())
k=int(input())
l,r=1,n*n
res=0
while l<=r:
    mid=(l+r)//2
    cnt=0
    for i in range(1,n+1):
        cnt+=min(mid//i,n)
    if cnt>=k:
        res=mid
        r=mid-1
    else:
        l=mid+1
print(res)