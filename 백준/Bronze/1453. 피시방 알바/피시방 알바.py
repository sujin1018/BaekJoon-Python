import sys
input=sys.stdin.readline
n=int(input())
a=[0]*101
cnt=0
s=[0]+list(map(int,input().split()))
for i in s:
    if a[i]==0:
        a[i]=1
    else:
        cnt+=1
print(cnt)