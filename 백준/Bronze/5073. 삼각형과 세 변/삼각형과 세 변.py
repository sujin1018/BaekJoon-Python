import sys
input=sys.stdin.readline
while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    s=[a,b,c]
    if 2*max(s) >= sum(s):
        print('Invalid')
    elif a==b==c:
        print('Equilateral')
    elif len(set(s))==2:
        print('Isosceles')
    else:
        print('Scalene')