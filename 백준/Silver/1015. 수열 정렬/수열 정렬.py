n=int(input())
a=list(map(int,input().split()))
s=sorted(a)
res=[0]*n
for i in range(n):
    idx=s.index(a[i])
    res[i]=idx
    s[idx]=-1
print(*res)