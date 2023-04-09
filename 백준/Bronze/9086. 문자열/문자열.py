import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
    a=input().rstrip()
    print(a[0]+a[-1])