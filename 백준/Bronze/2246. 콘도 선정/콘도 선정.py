import sys
input=sys.stdin.readline
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
a.sort()
c,res=10001,0
for i in a:
    if i[1]<c:
        c=i[1]
        res+=1
print(res)