import sys
input=sys.stdin.readline
n=int(input())
s={'ChongChong'}
for _ in range(n):
    a,b=map(str,input().split())
    if a in s:
        s.add(b)
    elif b in s:
        s.add(a)
print(len(s))