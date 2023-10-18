n=input()
flag=0
for i in range(1,len(n)):
    a,b=n[:i],n[i:]
    res1=res2=1
    for j in a:
        res1*=int(j)
    for j in b:
        res2*=int(j)
    if res1==res2:
        flag=1
        break
print("YES" if flag else "NO")