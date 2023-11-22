import sys
input=sys.stdin.readline
n=int(input())
for i in range(1,n+1):
    a=input().rstrip()
    print(str(i)+". "+a)