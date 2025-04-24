import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[int(input()) for _ in range(n)]
a.sort()
def bin_search(d):
    start,end=0,n-1
    while start<=end:
        mid=(start+end)//2
        if a[mid]<d:
            start=mid+1
        else:
            end=mid-1
    if start<n and a[start]==d:
        return start
    else:
        return -1
for _ in range(m):
    d=int(input())
    print(bin_search(d))