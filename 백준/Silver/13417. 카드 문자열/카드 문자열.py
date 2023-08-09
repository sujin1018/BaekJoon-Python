import sys
from collections import deque
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=input().rstrip().split()
    s=a[0]
    for i in range(1,n):
        if s[0]>=a[i]:
            s=a[i]+s
        else:
            s=s+a[i]
    print(s)