a,b=map(int,input().split())
cnt=1
while a!=b:
    cnt+=1
    tmp=b
    if b%2==0:
        b//=2
    elif b%10==1:
        b//=10
    if tmp==b:
        cnt=-1
        break
print(cnt)