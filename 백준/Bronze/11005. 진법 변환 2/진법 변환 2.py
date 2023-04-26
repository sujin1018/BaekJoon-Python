import sys
input=sys.stdin.readline
arr='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'    
n,b=map(int,input().split())
res=''
while n!=0:
    res+=arr[n%b]
    n//=b
print(res[::-1])  