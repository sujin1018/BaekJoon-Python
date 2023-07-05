import sys
input=sys.stdin.readline
a=input().rstrip()
b=list(input().rstrip())
s=[]
for i in range(len(a)):
    s.append(a[i])
    if s[-len(b):]==b:
        del s[-len(b):]
if s:
    print(*s,sep='')    
else:
    print('FRULA')