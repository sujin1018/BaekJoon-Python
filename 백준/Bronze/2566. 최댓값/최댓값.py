import sys
input=sys.stdin.readline
m=0
row,col=0,0
for i in range(9):
    a=list(map(int,input().rstrip().split()))
    if m < max(a):
        m=max(a)
        row=i
        col=a.index(m)
print(m)
print(row+1,col+1)