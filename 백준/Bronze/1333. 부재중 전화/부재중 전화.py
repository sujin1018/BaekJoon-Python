n,l,d=map(int,input().split())
l+=5
num=0
t=d
for i in range(n):
    num+=l
    while True:
        if t<num-5:
            t+=d
        else:
            break
    if t>=num-5 and t<num:
        break
print(t)