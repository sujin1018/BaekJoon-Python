import sys
input=sys.stdin.readline
for _ in range(int(input())):
    x,y=map(int,input().split())
    if x>=y:
        print('MMM BRAINS')
    else:
        print('NO BRAINS')