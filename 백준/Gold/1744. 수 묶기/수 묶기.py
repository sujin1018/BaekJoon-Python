import sys
input=sys.stdin.readline
n=int(input())
po,ne=[],[]
res=0
for _ in range(n):
    a=int(input())
    if a>1:
        po.append(a)
    elif a<=0:
        ne.append(a)
    else:
        res+=a
po.sort(reverse=True)
ne.sort()
for i in range(0,len(po),2):
    if i+1>=len(po):
        res+=po[i]
    else:
        res+=(po[i]*po[i+1])
for i in range(0,len(ne),2):
    if i+1>=len(ne):
        res+=ne[i]
    else:
        res+=(ne[i]*ne[i+1])
print(res)