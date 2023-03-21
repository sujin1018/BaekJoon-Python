import sys
input=sys.stdin.readline
n=int(input())
s=set()
for i in range(n):
    args=input().split()
    if(len(args)==1):
        if(args[0]=='all'):
            s=set([i for i in range(1,21)])
        elif(args[0]=='empty'):
            s.clear()
        continue
    else:
        a,b=args[0],int(args[1])
        if(a=='add'):
            s.add(b) 
        elif(a=='remove'):
            s.discard(b)    
        elif(a=='check'):
            print(1 if b in s else 0)
        elif(a=='toggle'):
            if b in s:
                s.discard(b)
            else:
                s.add(b)