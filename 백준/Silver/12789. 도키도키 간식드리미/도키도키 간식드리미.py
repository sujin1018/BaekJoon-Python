n=int(input())
a=list(map(int,input().split()))
b=[]
cnt=1
while a:
    if cnt==a[0]:
        cnt+=1
        a.pop(0)
    else:
        b.append(a.pop(0))
    while b:
        if b[-1]==cnt:
            cnt+=1
            b.pop()
        else:
            break
print("Sad" if b else "Nice")