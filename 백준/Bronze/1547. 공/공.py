import sys
input=sys.stdin.readline
n=int(input())
a=[1,2,3]
for _ in range(n):
    x,y=map(int,input().split())
    xi=a.index(x)
    yi=a.index(y)
    a[xi],a[yi]=a[yi],a[xi]
print(a[0])