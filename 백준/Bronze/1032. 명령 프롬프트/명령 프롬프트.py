import sys
input=sys.stdin.readline
n=int(input())
a=list(input().rstrip())
for _ in range(n-1):
    s=input().rstrip()
    for i in range(len(a)):
        if a[i]==s[i]:
            continue
        else:
            a[i]='?'
print(*a,sep='')