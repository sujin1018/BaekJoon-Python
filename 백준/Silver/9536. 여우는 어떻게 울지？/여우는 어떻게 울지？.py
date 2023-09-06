import sys
input=sys.stdin.readline
for _ in range(int(input())):
    lst=list(input().rstrip().split())
    while True:
        a=input().rstrip().split()
        if a[1]=="does":
            break
        while a[2] in lst:
            lst.remove(a[2])
    print(*lst)