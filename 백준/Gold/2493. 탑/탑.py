import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
res=[0]*n
stack=[]
for i in range(n):
    while stack:
        if a[i]>stack[-1][1]:
            stack.pop()
        else:
            res[i]=stack[-1][0]+1
            break
    stack.append((i,a[i]))
print(*res)            