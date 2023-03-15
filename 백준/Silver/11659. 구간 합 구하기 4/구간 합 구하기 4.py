import sys
input=sys.stdin.readline

n,m=map(int,input().split())
s=list(map(int,input().split()))
res=0
arr=[0]

for i in range(n):
    res += s[i]
    arr.append(res)
for i in range(m):
    i,j=map(int,input().split())
    print(arr[j]-arr[i-1])