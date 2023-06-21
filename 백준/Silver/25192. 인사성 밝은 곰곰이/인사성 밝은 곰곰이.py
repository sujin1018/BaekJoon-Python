import sys
input=sys.stdin.readline
n=int(input())
s=set()
cnt=0
for _ in range(n):
    a=input().rstrip()
    if a=='ENTER':
        s.clear()
    else:
        if a not in s:
            cnt+=1
            s.add(a)
print(cnt)