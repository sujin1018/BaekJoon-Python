a=[int(input()) for _ in range(9)]
r1,r2=0,0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if sum(a)-(a[i]+a[j])==100:
            r1=a[i]
            r2=a[j]
a.remove(r1)
a.remove(r2)
print('\n'.join(map(str,sorted(a))))