import sys
input = sys.stdin.readline
while True:
    a=input().rstrip()
    if a=='#':
        break
    cnt=0
    for i in a:
        if i in 'aeiouAEIOU':
            cnt+=1
    print(cnt)