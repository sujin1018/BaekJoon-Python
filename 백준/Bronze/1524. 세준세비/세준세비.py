import sys
input=sys.stdin.readline
for _ in range(int(input())):
    input()
    n,m=map(int,input().split())
    s=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if max(s)>=max(b):
        print('S')
    else:
        print('B')