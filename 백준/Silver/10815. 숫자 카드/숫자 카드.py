import sys
input=sys.stdin.readline
m=int(input())
m_n=set(map(int,input().split()))
n=int(input())
n_n=list(map(int,input().split()))
for i in n_n:
    if i in m_n:
        print(1, end=' ')
    else:
        print(0, end=' ')