n=int(input())
a=[[0]*10 for _ in range(n+1)]
a[1]=[0,1,1,1,1,1,1,1,1,1]
for i in range(2,n+1):
    for j in range(10):
        if j==0:
            a[i][j]=a[i-1][1]
        elif j==9:
            a[i][j]=a[i-1][8]
        else:
            a[i][j]=a[i-1][j-1]+a[i-1][j+1]
print(sum(a[n])%1000000000)