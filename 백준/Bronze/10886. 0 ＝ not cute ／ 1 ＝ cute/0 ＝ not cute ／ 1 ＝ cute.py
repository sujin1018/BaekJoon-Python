import sys
input=sys.stdin.readline
n=int(input())
a=[int(input()) for _ in range(n)]
if a.count(0)>a.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')