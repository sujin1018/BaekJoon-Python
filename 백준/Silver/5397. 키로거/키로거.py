import sys
input=sys.stdin.readline
for _ in range(int(input())):
    a=input().rstrip()
    l,r=[],[]
    for i in a:
        if i=="<":
            if l:
                r.append(l.pop())
        elif i==">":
            if r:
                l.append(r.pop())
        elif i=="-":
            if l:
                l.pop()
        else:
            l.append(i)
    l.extend(reversed(r))
    print(''.join(l))