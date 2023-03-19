import sys
from collections import Counter
input=sys.stdin.readline
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
a.sort()
d= Counter(a).most_common()
print(round(sum(a)/n))
print(a[n//2])
if(len(d)==1):
    print(d[0][0])
elif(d[0][1]==d[1][1]):
    print(d[1][0])
else:
    print(d[0][0])
print(max(a)-min(a))