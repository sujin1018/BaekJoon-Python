import sys
input=sys.stdin.readline
n=int(input())
a=[input().rstrip() for _ in range(n)]
cnt=1
while True:
    if len({i[-cnt:] for i in a})==n:
        print(cnt)
        break
    cnt+=1