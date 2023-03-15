import sys
n=int(input())
a=set()
for i in range(n):
    a.add(sys.stdin.readline().strip())
b=sorted(list(a), key=lambda x: (len(x), x))
for i in b:
    print(i)