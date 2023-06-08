import sys
input=sys.stdin.readline
n=int(input())
a=[int(input()) for _ in range(n)]
for i in reversed(sorted(a)):
    print(i)    