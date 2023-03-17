n=int(input())
res=1
for i in range(1,n+1):
    res*=i
a=str(res)[::-1]
cnt=0
for i in a:
    cnt+=1
    if(i=='0'):
        if(a[cnt]!='0'):
            res=a[cnt]
            break
        else:
            continue
    elif('0' not in a):
        res=a[0]
print(res)