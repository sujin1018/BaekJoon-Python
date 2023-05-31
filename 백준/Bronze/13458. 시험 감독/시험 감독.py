import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
cnt=n
for i in a:
    i-=b
    if i>0:
        cnt+=i//c
        if i%c!=0:
            cnt+=1
print(cnt)