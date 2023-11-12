import sys
input=sys.stdin.readline
n=int(input())
s=[list(map(int,input().split())) for _ in range(n)]
s.sort(key=lambda x:-x[2])
print(*s[0][:2])
print(*s[1][:2])
cnt=0
if s[0][0]==s[1][0]:
    cnt=2
for i in range(2,n+1):
    if cnt==0:
        print(*s[2][:2])
        break
    else:
        if s[i][0]!=s[1][0]:
            print(*s[i][:2])
            break