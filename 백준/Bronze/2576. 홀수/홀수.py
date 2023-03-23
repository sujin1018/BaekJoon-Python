import sys
input=sys.stdin.readline
a=[]
for i in range(7):
    s=int(input())
    if(s%2!=0):
        a.append(s)
if len(a)!=0:
    print(sum(a),min(a), sep='\n')
else:
    print(-1)