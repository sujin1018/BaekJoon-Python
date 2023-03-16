k=int(input())
a=[]
res=0
for i in range(k):
    s=int(input())
    a.append(s)
    if(s==0):
        a.pop()
        a.pop()
for i in a:
    res+=i
print(res)