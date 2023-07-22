n=int(input())
h=0
for i in range(1,n+1):
    if i<100:
        h=i
    else:
        s=list(map(int,str(i)))
        if s[0]-s[1]==s[1]-s[2]:
            h+=1
print(h)