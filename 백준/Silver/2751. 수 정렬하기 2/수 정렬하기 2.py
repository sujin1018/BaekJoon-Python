import sys
n=int(input())
a=[0]*n
for i in range(n):
    a[i]=int(sys.stdin.readline())
a.sort()
for i in a:
    print(i)