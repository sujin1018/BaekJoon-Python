import sys
input=sys.stdin.readline
n=int(input())
i=2
while True:
    if n==1:
        break
    if n%i==0:
        print(i)
        n//=i
        continue
    else:
        i+=1
        