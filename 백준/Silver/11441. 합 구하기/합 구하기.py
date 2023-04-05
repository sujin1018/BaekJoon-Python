import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
cum=[a[0]]
for i in range(1,n):
    cum.append(cum[-1]+a[i])
m=int(input())
for x in range(m):
    i,j=map(int,input().split())
    if i==1:
        print(cum[j-1])
    else:
        print(cum[j-1]-cum[i-2])