import sys
input=sys.stdin.readline
n,m=map(int,input().split())
s=set()
a=[]
cnt=0
for i in range(n):
    s.add(input())
for i in range(m):
    a.append(input())
for i in a:
    if i in s:
        cnt+=1
print(cnt)