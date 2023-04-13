import sys
input=sys.stdin.readline
n=int(input())
for i in range(n):
    a=input()
    for j in range(len(a)-1):
        if a[j] == a[j+1]:
            continue
        elif a[j] in a[j+1:]:
            n-=1
            break
print(n)