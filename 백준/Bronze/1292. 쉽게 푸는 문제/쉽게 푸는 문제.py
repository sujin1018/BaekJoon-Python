s=[]
a,b=map(int,input().split())
for i in range(1,b+1):
    for _ in range(i):
        s.append(i)
print(sum(s[a-1:b]))