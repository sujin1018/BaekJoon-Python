s=sorted(list(map(int,input().split())))
if s[0]+s[1]>s[2]:
    print(sum(s))
else:
    print((s[0]+s[1])*2-1)