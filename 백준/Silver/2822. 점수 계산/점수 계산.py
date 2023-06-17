d={}
s=0
a,b=[],[]
for i in range(1,9):
    d[i]=int(input())
res=sorted(d.items(), key=lambda x:x[1])
for k,v in res:
   a.append(v)
   b.append(k)
print(sum(a)-a[0]-a[1]-a[2])
b=b[3:8]
for i in sorted(b):
    print(i,end=' ')