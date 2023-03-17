import sys
input=sys.stdin.readline
n=int(input())
a=set(map(int,input().split()))
m=int(input())
m_li=list(map(int,input().split()))
for i in m_li:
    if i in a:
        print(1)
    else:
        print(0)