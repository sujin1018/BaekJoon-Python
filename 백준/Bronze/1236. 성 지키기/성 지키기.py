n,m=map(int,input().split())
a=[input() for _ in range(n)]
row,col=0,0
for i in range(n):
    if 'X' not in a[i]:
        row+=1
for j in range(m):
    if 'X' not in [a[i][j] for i in range(n)]:
        col+=1
print(max(row,col))