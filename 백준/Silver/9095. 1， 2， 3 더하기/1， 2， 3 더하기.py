import sys
input=sys.stdin.readline
a=[0]*12
a[1]=1
a[2]=2
a[3]=4
for i in range(4,11):
    a[i]=a[i-3]+a[i-2]+a[i-1]
for _ in range(int(input())):
    n=int(input())
    print(a[n])