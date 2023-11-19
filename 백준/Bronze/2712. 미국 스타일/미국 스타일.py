import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    a,b=input().rstrip().split()
    if b=='kg':
        print('%.4f'%(float(a)*2.2046),'lb')
    elif b=='l':
        print('%.4f'%(float(a)*0.2642),'g')
    elif b=='lb':
        print('%.4f'%(float(a)*0.4536),'kg')
    elif b=='g':
        print('%.4f'%(float(a)*3.7854), 'l')