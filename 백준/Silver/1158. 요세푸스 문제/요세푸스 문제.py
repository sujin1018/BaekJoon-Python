n,k=map(int,input().split())
a=[i for i in range(1,n+1)]
s=[]
num=0
for i in range(n):
    num+=(k-1)
    if num >= len(a):
        num%=len(a)
    s.append(str(a.pop(num)))
print('<'+', '.join(s)+'>',sep='')