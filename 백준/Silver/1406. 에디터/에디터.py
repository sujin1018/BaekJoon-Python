import sys
input=sys.stdin.readline
s1=list(input().rstrip())
s2=[]
c=len(s1)
for _ in range(int(input())):
    args=input().split()
    if(args[0]=='P'):
        s1.append(args[1])
    elif(args[0]=='L' and s1):
        s2.append(s1.pop())
    elif(args[0]=='D' and s2):
        s1.append(s2.pop())
    elif(args[0]=='B' and s1):
        s1.pop()
print(''.join(s1+list(reversed(s2))))