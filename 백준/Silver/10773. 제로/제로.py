import sys
input=sys.stdin.readline
k=int(input())
a=[]
for _ in range(k):
    s=int(input())
    if s == 0:
        a.pop()
    else:
        a.append(s)
print(sum(a))