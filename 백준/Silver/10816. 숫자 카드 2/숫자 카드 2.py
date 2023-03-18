import sys
from collections import Counter
input=sys.stdin.readline
n=int(input())
n_n=list(map(int,input().split()))
m=int(input())
m_n=list(map(int,input().split()))
d=Counter(n_n)
for i in m_n:
    if i in d:
        print(d[i], end=' ')
    else:
        print(0, end=' ')