import sys
input=sys.stdin.readline
n=int(input())
f,b=input().rstrip().split('*')
length=len(f)+len(b)
for _ in range(n):
    s=input().rstrip()
    if length>len(s):
        print('NE')
    else:
        if f==s[:len(f)] and b==s[-len(b):]:
            print('DA')
        else:
            print('NE')