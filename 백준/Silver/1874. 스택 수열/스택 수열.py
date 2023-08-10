import sys
input=sys.stdin.readline
idx=1
flag=True
n=int(input())
s,res=[],[]
for i in range(n):
    a=int(input())
    while idx<=a:
        s.append(idx)
        res.append('+')
        idx+=1
    if s[-1]==a:
        s.pop()
        res.append('-')
    else:
        flag=False
if not flag:
    print("NO")
else:
    print(*res,sep='\n')