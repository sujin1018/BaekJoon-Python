import sys
input=sys.stdin.readline
y=input().rstrip()
n=int(input().rstrip())
arr=[]
for i in range(n):
    a=input().rstrip()
    s=y+a
    L=s.count('L')
    O=s.count('O')
    V=s.count('V')
    E=s.count('E')
    res=((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
    arr.append([res,a])
arr.sort(key=lambda x:(-x[0],x[1]))
print(arr[0][1])