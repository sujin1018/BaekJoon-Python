import sys
input=sys.stdin.readline
s=[]
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    s.append((y,x))
s.sort()
for y,x in s:
    print(x,y)