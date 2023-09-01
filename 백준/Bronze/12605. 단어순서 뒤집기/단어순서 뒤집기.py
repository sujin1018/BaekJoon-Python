import sys
input=sys.stdin.readline
n=int(input())
for i in range(1,n+1):
    a=list(input().split())
    print('Case #%d: %s' %(i, ' '.join(a[::-1])))