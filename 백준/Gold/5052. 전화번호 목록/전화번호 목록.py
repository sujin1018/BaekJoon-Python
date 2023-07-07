import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    a=[input().strip() for _ in range(n)]
    a.sort()
    cons=True
    for i in range(n-1):
        if a[i]==a[i+1][:len(a[i])]:
            cons=False
            break
    if cons:
        print('YES')
    else:
        print('NO')