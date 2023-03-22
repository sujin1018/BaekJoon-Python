import sys
input=sys.stdin.readline
n=int(input())
s=[]
for i in range(n):
    args=input().split()
    if(len(args)!=1):
        a,b=args[0],int(args[1])
        if(a=='push_front'):
            s.insert(0,b)        
        elif(a=='push_back'):
            s.append(b)
    else:
        a=args[0]
        if(a=='pop_front'):
            if(len(s)!=0):
                print(s[0])
                s.pop(0)
            else:
                print(-1)
        elif(a=='pop_back'):
            if(len(s)!=0):
                print(s[-1])
                s.pop()
            else:
                print(-1)
        elif(a=='size'):
            print(len(s))
        elif(a=='empty'):
            print(1 if len(s)==0 else 0)
        elif(a=='front'):
            print(s[0] if len(s)!=0 else -1)
        elif(a=='back'):
            print(s[-1] if len(s)!=0 else -1)