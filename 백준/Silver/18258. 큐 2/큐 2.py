from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
s=deque([])
for _ in range(n):
    args=input().rstrip().split()
    if len(args)!=1:
        a,b=args[0],args[1]
        if a=='push':
            s.append(b)
    else:
        a=args[0]
        if a=='pop':
            print(s.popleft() if s else -1)
        elif a=='size':
            print(len(s))
        elif a=='empty':
            print(0 if s else 1)
        elif a=='front':
            print(s[0] if s else -1)
        else:
            print(s[-1] if s else -1)