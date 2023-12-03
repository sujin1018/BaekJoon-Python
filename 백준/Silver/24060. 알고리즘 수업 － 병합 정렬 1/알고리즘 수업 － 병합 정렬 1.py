def merge(arr):
    if len(arr)==1:
        return arr
    mid=(len(arr)+1)//2
    l=merge(arr[:mid])
    r=merge(arr[mid:])
    i=j=0
    s=[]
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            s.append(l[i])
            ans.append(l[i])
            i+=1
        else:
            s.append(r[j])
            ans.append(r[j])
            j+=1
    while i<len(l):
        s.append(l[i])
        ans.append(l[i])
        i+=1
    while j<len(r):
        s.append(r[j])
        ans.append(r[j])
        j+=1
    return s
n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
merge(a)
if len(ans)>=k:
    print(ans[k-1])
else:
    print(-1)