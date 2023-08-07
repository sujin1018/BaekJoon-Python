import sys
from collections import deque
input=sys.stdin.readline
s=deque([])
for _ in range(int(input())):
    args=input().rstrip().split()
    a=args[0]
    if a=='1':
        s.appendleft(args[1])
    elif a=='2':
        s.append(args[1])
    elif a=='3':
        print(s.popleft() if s else -1)
    elif a=='4':
        print(s.pop() if s else -1)
    elif a=='5':
        print(len(s))
    elif a=='6':
        print(0 if s else 1)
    elif a=='7':
        print(s[0] if s else -1)
    else:
        print(s[-1] if s else -1)