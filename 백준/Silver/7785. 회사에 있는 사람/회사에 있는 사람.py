import sys
input=sys.stdin.readline
n=int(input())
arr=set()
for _ in range(n):
    a,b=map(str,input().split())
    if b=='enter':
        arr.add(a)
    elif b=='leave':
        arr.remove(a)
arr=sorted(arr,reverse=True)
for i in arr:
    print(i)