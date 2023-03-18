n=int(input())
a=[]
for i in range(n):
    a.append(input())
a=sorted(a,key=lambda x:(a.count(x),x))
d={i:a.count(i) for i in a}
print(max(d, key=d.get))