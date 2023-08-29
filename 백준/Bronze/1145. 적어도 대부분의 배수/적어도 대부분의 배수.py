a=list(map(int,input().split()))
res=min(a)
while True:
    cnt=0
    for i in a:
        if res%i==0:
            cnt+=1
    if cnt>=3:
        print(res)
        break
    res+=1