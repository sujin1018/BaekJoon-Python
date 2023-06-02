s=[]
res=0
for i in range(4):
    a,b=map(int,input().split())
    res=res-a+b
    s.append(res)
print(max(s))