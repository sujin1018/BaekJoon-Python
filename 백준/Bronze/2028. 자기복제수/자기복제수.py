import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a=len(str(n))
    if str(n**2)[-a:]==str(n):
        print('YES')
    else:
        print('NO')