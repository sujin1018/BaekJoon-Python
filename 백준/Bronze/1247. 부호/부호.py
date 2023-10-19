import sys
input=sys.stdin.readline
for _ in range(3):
    n=int(input())
    a=[int(input()) for _ in range(n)]
    if sum(a)==0:
        print(0)
    elif sum(a)>0:
        print("+")
    else:
        print("-")