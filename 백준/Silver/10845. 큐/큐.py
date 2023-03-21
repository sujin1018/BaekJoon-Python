import sys
input=sys.stdin.readline
n=int(input())
s=[]
for i in range(n):
    args=input().split()
    if(len(args)!=1):
        a,b=args[0],args[1]
        if(a=='push'):
            s.append(b)
        continue
    else:
        a=args[0]
        if(a=='pop'):
            if(len(s)==0):
                print(-1)
            else:
                print(s[0])
                s.pop(0)
        elif(a=='size'):
            print(len(s))
        elif(a=='empty'):
            print(1 if len(s)==0 else 0)
        elif(a=='front'):
            print(s[0] if len(s)>0 else -1)
        elif(a=='back'):
            print(s[-1] if len(s)>0 else -1)