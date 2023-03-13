p,q=map(int,input().split())
a=[]
for i in range(1,p+1):
    if(p%i==0):
        a.append(i)

if(len(a) >= q):
    print(a[q-1])
else:
    print("0")
