import sys
input=sys.stdin.readline
n=int(input())
a=[input()[0] for _ in range(n)]
res=[]
s=set(a)
for i in s:
    if a.count(i)>=5:
        res.append(i)
if res:
    print(''.join(sorted(res)))
else:
    print('PREDAJA')