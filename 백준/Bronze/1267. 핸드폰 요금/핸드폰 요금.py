n=int(input())
a=list(map(int,input().split()))
y=m=0
for i in a:
    y+=(i//30+1)*10
    m+=(i//60+1)*15
if y==m:
    print('Y M',m)
elif y>m:
    print('M',m)
else:
    print('Y',y)