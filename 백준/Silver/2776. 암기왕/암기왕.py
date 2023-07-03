import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    n_n=set(map(int,input().split()))
    m=int(input())
    m_n=list(map(int,input().split()))
    for i in m_n:
        if i in n_n:
            print(1)
        else:
            print(0)