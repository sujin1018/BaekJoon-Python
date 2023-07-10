import sys
input=sys.stdin.readline
n=int(input())
a=[list(input().rstrip().split()) for _ in range(n)]
a.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in a:
    print(i[0])