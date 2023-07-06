import sys
n=list(map(int,sys.stdin.readline().strip()))
if 0 in n:
    if sum(n)%3==0:
        n.sort(reverse=True)
        print(*n,sep='')
    else:
        print(-1)
else:
    print(-1)