n,s=map(int,input().split())
a=list(map(int,input().split()))
cnt=0
res=[]
def back(x):
    global cnt
    if sum(res)==s and res:
        cnt+=1
    for i in range(x,n):
        res.append(a[i])
        back(i+1)
        res.pop()
back(0)
print(cnt)