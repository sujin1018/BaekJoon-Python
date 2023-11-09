import sys
input=sys.stdin.readline
num={'0':4,'1':2, '2':3,'3':3,'4':3,'5':3,'6':3,'7':3,'8':3,'9':3}
while True:
    n=input().rstrip()
    if n=='0':
        break
    res=0
    for i in n:
        res+=(num[i]+1)
    print(res+1)