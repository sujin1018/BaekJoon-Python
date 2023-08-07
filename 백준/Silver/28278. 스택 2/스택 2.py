import sys
input=sys.stdin.readline
s=[]
for _ in range(int(input())):
    args=input().split()
    a=args[0]
    if a=='2':
        print(s.pop() if s else -1)
    elif a=='3':
        print(len(s))
    elif a=='4':
        print(0 if s else 1)
    elif a=='5':
        print(s[-1] if s else -1)
    else:
        s.append(args[1])