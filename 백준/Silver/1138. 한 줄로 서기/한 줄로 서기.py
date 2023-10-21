n=int(input())
a=list(map(int,input().split()))
s=[0]*n
for i in range(1,n+1):
    cnt=0
    for j in range(n):
        if cnt==a[i-1] and s[j]==0:
            s[j]=i
            break
        elif s[j]==0:
            cnt+=1
print(*s)