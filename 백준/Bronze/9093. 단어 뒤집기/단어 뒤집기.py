import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
    a=input().rstrip().split()
    for i in a:
        print(i[::-1], end=' ')
    print()