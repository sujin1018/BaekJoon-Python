import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
b=sorted(set(a))
d={b[i]: i for i in range(len(b))}
for i in a:
    print(d[i], end=' ')