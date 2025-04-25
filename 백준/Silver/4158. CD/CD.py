import sys
input=sys.stdin.readline
while True:
    n,m=map(int,input().split())
    cd_n={int(input()) for _ in range(n)}
    cd_m={int(input()) for _ in range(m)}
    if n==0 and m==0:
        break
    print(len(cd_n&cd_m))