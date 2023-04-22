import sys
input=sys.stdin.readline
res=0
for i in range(5):
    a=int(input())
    if a<=40:
        a=40
    res+=a
print(res//5)
